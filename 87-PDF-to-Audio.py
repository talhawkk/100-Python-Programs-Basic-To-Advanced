from gtts import gTTS
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import PyPDF2
import os

class MusicPlayer:
    def __init__(self, window):
        window.geometry('400x150')
        window.title('PDF and Music Player')
        window.resizable(0, 0)

        # Buttons
        Load = Button(window, text='Load Audio', width=10, font=('Times', 10), command=self.load)
        Play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
        Pause = Button(window, text='Pause/Resume', width=15, font=('Times', 10), command=self.pause)
        Stop = Button(window, text='Stop', width=10, font=('Times', 10), command=self.stop)
        Speech = Button(window, text='Select PDF for Speech', width=20, font=('Times', 10), command=self.speech)

        # Button Placement
        Load.place(x=10, y=20)
        Play.place(x=120, y=20)
        Pause.place(x=230, y=20)
        Stop.place(x=350, y=20)
        Speech.place(x=120, y=70)

        # Initialize attributes
        self.music_file = None
        self.playing_state = False
        mixer.init()  # Initialize pygame mixer once

    def load(self):
        # Load audio file
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path and file_path.lower().endswith(('.mp3', '.wav')):
            self.music_file = file_path
            print(f"Loaded file: {self.music_file}")
        else:
            print("Unsupported file format. Please select an MP3 or WAV file.")

    def play(self):
        if self.music_file:
            try:
                mixer.music.load(self.music_file)
                mixer.music.play()
                print("Playing audio...")
            except Exception as e:
                print(f"Could not play file: {e}")
        else:
            print("No audio file loaded. Please load an MP3 or WAV file.")

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()

    def speech(self):
        # Load and convert PDF to audio
        pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if pdf_file and pdf_file.endswith('.pdf'):
            try:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text_list = []

                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:
                        text_list.append(text)

                text_string = " ".join(text_list)

                # Generate audio with gTTS
                language = 'en'
                audio = gTTS(text=text_string, lang=language, slow=False)
                audio_path = os.path.splitext(pdf_file)[0] + "_audio.mp3"
                audio.save(audio_path)
                print(f"Audio saved as: {audio_path}")
            except Exception as e:
                print(f"Error processing PDF: {e}")
        else:
            print("Invalid PDF file. Please select a valid PDF.")

# Running the application
root = Tk()
app = MusicPlayer(root)
root.mainloop()
