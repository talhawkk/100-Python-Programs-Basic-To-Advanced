from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image
from PIL.ExifTags import TAGS
import os

def extract_audio_metadata(file_path):
    try:
        audio = MP3(file_path, ID3=ID3)
        print("\nAudio Metadata:")
        for tag, value in audio.items():
            if tag == "APIC:":
                # Save artwork as an image file
                artwork_file = os.path.join(os.path.dirname(file_path), "album_art.jpg")
                with open(artwork_file, "wb") as img:
                    img.write(value.data)
                print(f"{tag}: Album artwork saved as {artwork_file}")
            else:
                print(f"{tag}: {value}")
    except Exception as e:
        print(f"Error reading audio metadata: {e}")

def extract_image_metadata(file_path):
    try:
        with Image.open(file_path) as img:
            print("\nImage Metadata:")
            exif_data = img._getexif()
            if exif_data is not None:
                for tag_id, value in exif_data.items():
                    tag_name = TAGS.get(tag_id, tag_id)
                    print(f"{tag_name}: {value}")
            else:
                print("No EXIF metadata found.")
    except Exception as e:
        print(f"Error reading image metadata: {e}")

def main():
    file_path = input("Enter the path of the file (audio or image): ").strip()
    if not os.path.isfile(file_path):
        print("The provided path does not exist or is not a valid file.")
        return

    if file_path.lower().endswith(".mp3"):
        extract_audio_metadata(file_path)
    elif file_path.lower().endswith((".jpg", ".jpeg", ".png")):
        extract_image_metadata(file_path)
    else:
        print("Please provide a valid MP3 or image file.")

if __name__ == "__main__":
    main()
