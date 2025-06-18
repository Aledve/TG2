# ejemplo_cqrs.py

# 1) Almacén de datos compartido (en memoria, muy simple)
class MessageStore:
    def __init__(self):
        self._message = ""

# 2) Componente de comandos: cambia el estado
class CommandHandler:
    def __init__(self, store: MessageStore):
        self._store = store

    def set_message(self, mensaje: str):
        """Establece un nuevo mensaje en el store."""
        self._store._message = mensaje

# 3) Componente de consultas: lee el estado
class QueryHandler:
    def __init__(self, store: MessageStore):
        self._store = store

    def get_message(self) -> str:
        """Devuelve el mensaje actual."""
        return self._store._message

# 4) Uso del patrón CQRS
if __name__ == '__main__':
    store = MessageStore()
    cmd = CommandHandler(store)
    qry = QueryHandler(store)

    # Comando: guardamos "¡Hola, mundo!"
    cmd.set_message("¡Hola, mundo!")

    # Consulta: recuperamos e imprimimos el mensaje
    print(qry.get_message())
