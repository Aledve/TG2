# ejemplo_graphql_client.py

import requests

# Definimos la consulta GraphQL
query = '{ hello }'

# Hacemos POST al endpoint
response = requests.post(
    'http://127.0.0.1:5000/graphql',
    json={'query': query}
)

# Imprimimos el valor devuelto
print(response.json()['data']['hello'])  # ¡Hola, mundo!
