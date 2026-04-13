import secrets
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, String

from database import Base


class APIKey(Base):
    __tablename__ = "api_keys"

    key = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)

    @staticmethod
    def generate() -> str:
        return secrets.token_urlsafe(32)
