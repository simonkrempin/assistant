import pyttsx3
from lib import greeting
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)

engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

greeting.greet_user(speak)

stop = False

while not stop:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='de-DE')
        print(f"User said: {query}\n")

        if 'stop' in query or 'exit' in query:
            stop = True
        else:
            speak("I don't understand")
    except:
        print("Say that again please...")
        continue
