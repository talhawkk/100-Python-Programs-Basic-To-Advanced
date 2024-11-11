import pygame
from datetime import datetime
import time

def set_alarm(alarm_time, sound_file="D:/Github pushed/100-Python-programs-Basic-to-Advanced/sss.wav"):
    pygame.mixer.init()
    
    # Try to load the sound file
    try:
        pygame.mixer.music.load(sound_file)
    except pygame.error as e:
        print(f"Could not load sound file: {e}")
        return
    
    print(f"Alarm set for {alarm_time}.")

    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Time's up! Alarm ringing...")
            pygame.mixer.music.play()
            break
        time.sleep(10)  # Check every 10 seconds
    
    # Allow time for the sound to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Example usage
alarm_time = input("Set alarm time (HH:MM): ")
set_alarm(alarm_time)
