# ejemplo_soap_service.py

from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @rpc(_returns=Unicode)
    def say_hello(ctx):
        return "¡Hola, mundo!"

# Definimos la aplicación SOAP
app = Application(
    [HelloWorldService],
    tns='spyne.examples.helloworld',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(app)
    print("Servicio SOAP escuchando en http://127.0.0.1:8000")
    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()
