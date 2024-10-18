import pyttsx3
l=["talha","hamza","ali"]
engine = pyttsx3.init()
# for i in l:

#     engine.say(f"Hello kesa ha  {i}")
# engine.runAndWait()


x = str(input("Enter the text you want to convert to speech: "))
engine.say(x)

engine.runAndWait()