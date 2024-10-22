import speech_recognition as sr
import win32com.client
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1.6
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
        except:
            print("finding trouble in Recognizing....")
while True:
    print("listening.....")
    take_command()
