# ejemplo_webhook_receiver.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Leemos opcionalmente el JSON enviado
    payload = request.get_json(silent=True) or {}
    print("Payload recibido:", payload)
    # Respondemos con nuestro "Hola, mundo"
    return "¡Hola, mundo!", 200

if __name__ == '__main__':
    # Arrancamos el servidor en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
