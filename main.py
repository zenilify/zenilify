from datetime import datetime, timezone

from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import APIKey

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Zapier API Key Service", version="1.0.0")

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


# ---------- Schemas ----------

class KeyCreateRequest(BaseModel):
    name: str


class KeyResponse(BaseModel):
    key: str
    name: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


# ---------- Auth helper ----------

def require_valid_key(
    key: str | None = Security(api_key_header),
    db: Session = Depends(get_db),
) -> APIKey:
    if not key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing API key")
    record = db.query(APIKey).filter(APIKey.key == key, APIKey.is_active == True).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or revoked API key")
    return record


# ---------- Endpoints ----------

@app.post("/api-keys", response_model=KeyResponse, status_code=status.HTTP_201_CREATED)
def create_api_key(body: KeyCreateRequest, db: Session = Depends(get_db)):
    """Create a new API key. The key is returned only once — store it securely."""
    record = APIKey(key=APIKey.generate(), name=body.name)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@app.get("/api-keys", response_model=list[KeyResponse])
def list_api_keys(db: Session = Depends(get_db)):
    """List all API keys (active and revoked)."""
    return db.query(APIKey).all()


@app.delete("/api-keys/{key}", status_code=status.HTTP_204_NO_CONTENT)
def revoke_api_key(key: str, db: Session = Depends(get_db)):
    """Revoke an API key so it can no longer be used."""
    record = db.query(APIKey).filter(APIKey.key == key).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="API key not found")
    record.is_active = False
    db.commit()


# ---------- Zapier auth check ----------

@app.get("/zapier/auth-test")
def zapier_auth_test(current_key: APIKey = Depends(require_valid_key)):
    """
    Zapier calls this endpoint during the 'Test' step of API Key authentication.
    Pass your key in the X-API-Key header.
    """
    return {"authenticated": True, "key_name": current_key.name}


# ---------- Example protected resource ----------

@app.get("/zapier/triggers/sample")
def sample_trigger(current_key: APIKey = Depends(require_valid_key)):
    """Example Zapier trigger endpoint protected by API key auth."""
    return [
        {"id": 1, "message": "Hello from Zenilify", "timestamp": datetime.now(timezone.utc).isoformat()}
    ]
