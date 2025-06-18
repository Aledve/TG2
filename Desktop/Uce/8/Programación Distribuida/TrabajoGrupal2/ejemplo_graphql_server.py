# ejemplo_graphql_server.py

from flask import Flask
from flask_graphql import GraphQLView
import graphene

# 1) Definimos el esquema con una sola Query “hello”
class Query(graphene.ObjectType):
    hello = graphene.String(description="Retorna un saludo")

    def resolve_hello(self, info):
        return "¡Hola, mundo!"

schema = graphene.Schema(query=Query)

# 2) Creamos la app Flask y añadimos la vista GraphQL
app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # habilita la interfaz web de pruebas
    )
)

if __name__ == '__main__':
    print("Servidor GraphQL escuchando en http://127.0.0.1:5000/graphql")
    app.run(host='127.0.0.1', port=5000)
