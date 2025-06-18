# ejemplo_grpc_client.py

import grpc

# Importamos las clases generadas
import ejemplo_pb2
import ejemplo_pb2_grpc

def run():
    # 1) Conectamos con el servidor
    channel = grpc.insecure_channel('localhost:50051')
    stub = ejemplo_pb2_grpc.HelloServiceStub(channel)

    # 2) Llamamos al RPC con un HelloRequest(name="mundo")
    response = stub.SayHello(ejemplo_pb2.HelloRequest(name="mundo"))

    # 3) Imprimimos el mensaje recibido
    print(response.message)  # ¡Hola, mundo!

if __name__ == '__main__':
    run()
