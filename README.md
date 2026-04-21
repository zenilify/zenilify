# 👋 Hi, I’m @zenilify

- 👀 I’m interested in tech, python and more
- 🌱 I’m currently learning everything from linux basics to...
- 💞️ I’m looking to collaborate on easy stuff to learn more, learning by doing


## tldraw Canvas App

A React + Vite app with [tldraw](https://tldraw.dev/) — an infinite canvas SDK.

### Setup

```bash
cd tldraw-app
cp .env.example .env        # add your VITE_TLDRAW_LICENSE_KEY
npm install
npm run dev                  # opens at http://localhost:5173
```

### Build for production

```bash
npm run build
npm run preview
```

### How to use the canvas

| Action | How |
|--------|-----|
| Draw | Select a tool from the toolbar (pencil, shapes, text) |
| Pan | Hold Space + drag, or use middle mouse button |
| Zoom | Scroll wheel or pinch on trackpad |
| Select | Press `V` or click the arrow tool |
| Undo/Redo | `Ctrl+Z` / `Ctrl+Y` |
| Export | Menu → Edit → Export |

The license key is read from `VITE_TLDRAW_LICENSE_KEY` in your `.env` file. It is safe to include in frontend code — tldraw validates it client-side against your allowed domains, no server secret involved.

<!---
zenilify/zenilify is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
