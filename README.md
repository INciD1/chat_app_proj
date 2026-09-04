
# 💬 Chat App Proj

A real-time chat application built with Python, Flask, and Flask-SocketIO. Users can create a new chat room or join an existing one with a room code, then chat live over WebSocket.

## 🚀 Features

- Create a new room (random 4-character room code) or join an existing one by code
- Real-time messaging over WebSocket (Flask-SocketIO)
- Join/leave notifications in the room
- Built-in emoji picker
- GIF search and sending via the Giphy API (proxied through our own backend endpoint, never called directly from the browser)
- Multiple rooms supported concurrently, with per-room user state tracked via session

## 🛠️ Tech Stack

- Python 3.9
- Flask, Flask-SocketIO
- gevent / gevent-websocket (for WebSocket support in deployment)
- HTML, CSS, JavaScript
- Giphy API (for the GIF feature — called through a backend proxy)
- Deployed on [Render](https://render.com) (see `render.yaml`)

## 📁 Project Structure

```
chat_app_proj/
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── base.html
│   ├── home.html
│   └── room.html
├── main.py
├── requirements.txt
├── render.yaml
├── runtime.txt
├── .env.example
└── README.md
```

## ⚙️ Setup & Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/INciD1/chat_app_proj.git
   cd chat_app_proj
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix / macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and add your own Giphy API key (free at https://developers.giphy.com/):
   ```bash
   cp .env.example .env
   ```

5. Run the app:
   ```bash
   python main.py
   ```

6. Open your browser at `http://localhost:5000`

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Flask session secret (auto-generated on Render) |
| `GIPHY_API_KEY` | Giphy API key — must be set both locally and on Render (no default; if unset, the GIF picker won't work but the rest of the chat still runs fine) |
| `PORT` | Port the app runs on (defaults to 5000 locally) |

> ✅ The Giphy API key now lives server-side (read from an environment variable). The frontend calls our own `/api/gif-search` endpoint instead of hitting `api.giphy.com` directly, so the key is never shipped to the browser.

## 📌 Current Limitations

- Rooms and messages live entirely in memory (the `rooms` dict) — a server restart wipes every room and message history
- No real authentication (just a display name, no password)
- Runs on a single worker (`-w 1` in `render.yaml`) since state lives in one process's memory — can't scale horizontally without moving to a shared store like Redis

## 🗺️ Possible Improvements

- Persist rooms/messages to a real store (Redis or PostgreSQL) instead of an in-memory dict
- Add real user registration/login
- Support multiple workers by moving room state to Redis (via Flask-SocketIO's message queue support)

## 🙌 Contributing

This project is still under active development. Issues and pull requests are welcome.
