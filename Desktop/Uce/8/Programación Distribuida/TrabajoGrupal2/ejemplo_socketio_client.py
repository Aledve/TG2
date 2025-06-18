# ejemplo_socketio_client.py

import socketio

# Cliente Socket.IO
sio = socketio.Client()

# Al conectarse, enviamos un mensaje cualquiera
@sio.event
def connect():
    print('Conectado al servidor')
    sio.send('ping')

# Al recibir cualquier mensaje, lo imprimimos y desconectamos
@sio.event
def message(data):
    print('Mensaje del servidor:', data)
    sio.disconnect()

if __name__ == '__main__':
    sio.connect('http://127.0.0.1:5000')
    sio.wait()
