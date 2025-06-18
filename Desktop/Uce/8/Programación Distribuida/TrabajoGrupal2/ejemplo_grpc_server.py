# ejemplo_grpc_server.py

import grpc
from concurrent import futures
import time

# Importamos las clases generadas (ver instrucciones más abajo)
import ejemplo_pb2
import ejemplo_pb2_grpc

# 1) Implementamos el servicer definido en el .proto
class HelloServiceServicer(ejemplo_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        # Construimos la respuesta usando el nombre recibido
        return ejemplo_pb2.HelloReply(message=f"¡Hola, {request.name}!")

def serve():
    # 2) Creamos el servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    ejemplo_pb2_grpc.add_HelloServiceServicer_to_server(HelloServiceServicer(), server)
    server.add_insecure_port('[::]:50051')  # escuchamos en el puerto 50051
    server.start()
    print("Servidor gRPC escuchando en el puerto 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
