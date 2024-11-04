import pyttsx3
import PyPDF2

file = open("D:/Github pushed/100-Python-programs-Basic-to-Advanced/affidavit.pdf", mode="rb")
pdf_reader = PyPDF2.PdfReader(file)

# Pages=len(pdf_reader.pages)
# print(Pages)
page = pdf_reader.pages[0]  
text = page.extract_text()

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()

file.close()

