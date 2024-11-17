import os
from pathlib import Path

def organize_folder(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            ext = file.split('.')[-1] if '.' in file else "Others"
            folder = os.path.join(directory, ext.upper())
            os.makedirs(folder, exist_ok=True)
            os.rename(file_path, os.path.join(folder, file))
            print(f"Moved: {file} -> {folder}")

directory = input("Enter the folder path to organize: ")
organize_folder(directory)
