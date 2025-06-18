# ejemplo_webhook_sender.py

import requests

response = requests.post(
    'http://127.0.0.1:5000/webhook',
    json={"trigger": "test"}
)
print(response.text)  # Debería mostrar: ¡Hola, mundo!
