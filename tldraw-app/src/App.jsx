import { Tldraw } from 'tldraw'
import 'tldraw/tldraw.css'

const LICENSE_KEY = import.meta.env.VITE_TLDRAW_LICENSE_KEY

export default function App() {
  return (
    <div style={{ position: 'fixed', inset: 0 }}>
      <Tldraw licenseKey={LICENSE_KEY} />
    </div>
  )
}
