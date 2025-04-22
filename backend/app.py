from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

# Initialize the app
app = Flask(__name__)
CORS(app)  # Enable CORS for the frontend

# Initialize SocketIO
socketio = SocketIO(app)

# Example Route
@app.route('/')
def home():
    return jsonify(message="Welcome to Match-Ease backend!")

# Run the app
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
