import speech_recognition as sr
import pyttsx3 as pyt
from Interfaz import *
import funciones as f

# Inicializar el reconocimiento de voz
listener = sr.Recognizer()

# Inicializar el motor de texto a voz
engine = pyt.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Definir la función para ejecutar el comando dado por el usuario
def run():
    command = f.listen()
    if "reproducir música" in command:
        f.speak("Reproduciendo música")
    elif "abrir navegador" in command:
        f.speak("Abriendo navegador")
    elif "apagar" in command:
        f.speak("Apagando asistente")
        Interfaz.window.destroy()

if __name__ == '__main__':
    # Ejecutar la interfaz gráfica
    window.mainloop()