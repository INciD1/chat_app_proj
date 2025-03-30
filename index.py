from main import app, socketio

# This is needed for Vercel to handle both HTTP and WebSocket
app = socketio.run(app)