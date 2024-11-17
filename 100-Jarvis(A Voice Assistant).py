import webbrowser
import speech_recognition as sr
import win32com.client
import os
def say(txt):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(txt)

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
            return query
        except:
            return "Some error Occurred, sorry from jarvis"


# say(str(input("Enter the word you want to speak it out by computer")))
say("Hello, i am jarvis Ai")
while True:
    print("listening")
    query=take_command()
    sites=[["google","https://www.google.com"],["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["instagram","https://www.instagram.com"],["facebook","https://www.facebook.com"],["linkedin","https://www.linkedin.com"],
           ["chat gpt","https://www.chatgpt.com"],["whatsapp","https://web.whatsapp.com/"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"opening {site[0]}")
            webbrowser.open(site[1])
    if "open music".lower() in query.lower():
        say("opening music")
        path="C:/Users/Talha/Downloads/Pehle Bhi Main - Animal 128 Kbps.mp3"
        os.startfile(path)
    if "Stop".lower() in query.lower():
        print("jarvis is going to shutdown....\n\nshutdown")
        break
    if "shutdown".lower() in query.lower():
        print("System is going to shutdown....\n\nshutdown")
        os.system("shutdown /s /t 1")


# say(query)