import speech_recognition as sr
import pyttsx3 as pyt
import pywhatkit, wikipedia, datetime, keyboard
from pygame import mixer

listener = sr.Recognizer()
engine = pyt.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text) :
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source :
            print('Escuchando...')
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='es')
            rec = rec.lower()
            if 'pablo' in rec :
                rec = rec.replace('pablo','')
    except:
        pass 
    return rec

def run_pablo() :
    while True:
        rec = listen()
        if 'reproduce' in rec :
            music = rec.replace('reproduce', '')
            print(f'Reproduciendo {music}')
            talk(f'Reproduciendo {music}')
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang('es')
            wiki = wikipedia.summary(search, 1)
            print(search + ': ' + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            clock = rec.replace('alarma', '')
            clock = clock.strip()
            talk('Alarma activada a las ' + clock + ' horas')
            while True :
                if datetime.datetime.now().strftime('%H:%M') == clock:
                    print('DESPIERTA!!!')
                    mixer.init()
                    mixer.music.load('alarma\\alarma.mp3')
                    mixer.music.play()
                    if keyboard.read_key() == 's' :
                        mixer.music.stop()
                        break

if _name_ == '_main_':
    run_pablo()