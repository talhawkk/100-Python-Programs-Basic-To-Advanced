import speech_recognition as sr
# import pyaudio
from deep_translator import GoogleTranslator
import pyttsx3

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=.8
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
            return query
        except:
            print("finding trouble in Recognizing....")

while True:
    print("listening...")
    query=take_command()
    translator = GoogleTranslator(source='en', target='fr')
    translation = translator.translate(query)
    print(translation)
    engine = pyttsx3.init()

    engine.say(translation)

    engine.runAndWait()

