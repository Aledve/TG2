# ejemplo_socketio_server.py

from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Manejador para cualquier mensaje recibido
@socketio.on('message')
def handle_message(msg):
    # Cuando llegue un mensaje, respondemos con "¡Hola, mundo!"
    send('¡Hola, mundo!')

if __name__ == '__main__':
    print("Servidor Socket.IO escuchando en http://127.0.0.1:5000")
    socketio.run(app, host='127.0.0.1', port=5000)
