import tkinter as tk
from funciones import *
import Asistente_virtual as asist

# Inicializar la interfaz gráfica
window = tk.Tk()
window.title("Asistente de voz")
window.geometry("400x300")

# Crear el botón para que el usuario active el asistente de voz
button = tk.Button(
    text="Activar asistente",
    width=25,
    height=5,
    bg="blue",
    fg="white",
    command=asist.run
)

button.pack()

