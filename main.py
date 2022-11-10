import pyttsx3
from lib import greeting

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)

engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

greeting.greet_user(speak)
