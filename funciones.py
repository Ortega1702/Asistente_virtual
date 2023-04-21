import os
import datetime
import keyboard
import wikipedia
import pywhatkit
import speech_recognition as sr
import threading
import pyttsx3 as pyt
from pygame import mixer
import Asistente_virtual as asist
import Interfaz

#Funcion para leer notificaciones
def read_notifications():
    command = "powershell Get-EventLog -LogName Application -Source DesktopNotifications | Select-Object -Last 1 | Format-List"
    output = os.popen(command).read()
    if "DesktopNotifications" in output:
        text = "Nueva notificación. "
        start = output.find("Message : ") + 10
        end = output.find("\n", start)
        message = output[start:end]
        text += message
        asist.engine.say(text)
        asist.engine.runAndWait()
        
# Función para reproducir un sonido
def play_sound(sound_file):
    mixer.init()
    mixer.music.load(sound_file)
    mixer.music.play()

# Función para hablar
def talk(text):
    asist.engine.say(text)
    asist.engine.runAndWait()

# Función para escuchar el micrófono
def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            pc = asist.listener.listen(source)
            rec = asist.listener.recognize_google(pc, language='es')
            rec = rec.lower()
            if 'pablo' in rec:
                rec = rec.replace('pablo', '')
    except:
        rec = ''
    return rec

# Función para reproducir música en YouTube
def play_music(music):
    print(f'Reproduciendo {music}')
    talk(f'Reproduciendo {music}')
    pywhatkit.playonyt(music)

# Función para buscar información en Wikipedia
def search_wiki(search):
    wikipedia.set_lang('es')
    wiki = wikipedia.summary(search, 1)
    print(search + ': ' + wiki)
    talk(wiki)

# Función para configurar la alarma
def set_alarm():
    clock = e.get()
    if clock == '':
        return
    talk('Alarma activada a las ' + clock + ' horas')
    while True:
        if datetime.datetime.now().strftime('%H:%M') == clock:
            print('DESPIERTA!!!')
            play_sound('alarma/alarma.mp3')
            threading.Thread(target=stop_alarm).start()
            break

# Función para detener la alarma
def stop_alarm():
    while True:
        if keyboard.is_pressed('s'):
            mixer.music.stop()
            break

# Función para enviar un mensaje de WhatsApp
def send_message(contact, message):
    talk(f'Enviando mensaje a {contact}')
    pywhatkit.sendwhatmsg(f"+1{contact}", message, datetime.datetime.now().hour, datetime.datetime.now().minute+1)

# Función para abrir una aplicación
def open_app(app):
    talk(f'Abriendo {app}')
    os.system(f'open -a "{app}.app"')

# Función para cambiar a una ventana de una aplicación
def switch_window(window):
    talk(f'Cambiando a la ventana de {window}')
    os.system(f"osascript -e 'tell application \"{window}\" to activate'")

# Definir la función para que el asistente responda
def speak(text):
    asist.engine.say(text)
    asist.engine.runAndWait()

# Definir la función para que el asistente escuche y procese el audio
def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = asist.listener.listen(source)
            command = asist.listener.recognize_google(voice, language="es-ES")
            command = command.lower()
            if "asistente de voz" in command:
                command = command.replace("asistente de voz", "")
                print(command)
    except:
        pass
    return command



