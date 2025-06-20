# ejemplo_event_driven.py

import tkinter as tk

# 1) Emisor de eventos
class EventEmitter:
    def __init__(self):
        self._events = {}

    def on(self, event_name, handler):
        self._events.setdefault(event_name, []).append(handler)

    def emit(self, event_name, *args, **kwargs):
        for handler in self._events.get(event_name, []):
            handler(*args, **kwargs)


# 2) Handler para el saludo
def saludo_handler(mensaje):
    label.config(text=mensaje)


# 3) Configuramos nuestro bus de eventos
emitter = EventEmitter()
emitter.on('saludo', saludo_handler)


# 4) Función que se llama al hacer click
def on_button_click():
    emitter.emit('saludo', '¡Hola, mundo!')


# 5) Construimos la interfaz gráfica
root = tk.Tk()
root.title("Event Driven Interactivo")

button = tk.Button(root, text="Haz click", command=on_button_click)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

# 6) Entramos en el bucle de eventos de Tkinter
root.mainloop()
