# ejemplo_soap_client.py

from zeep import Client

# Cambia la URL si tu servicio corre en otra dirección/puerto
wsdl = 'http://127.0.0.1:8000/?wsdl'
client = Client(wsdl=wsdl)

# Llamamos al método say_hello del servicio SOAP
respuesta = client.service.say_hello()
print(respuesta)  # Debería mostrar: ¡Hola, mundo!
