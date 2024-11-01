from yt_dlp import YoutubeDL

link = input("Enter link of video: ")

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',  
    }

with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(link, download=True)  
    print("Video Title:", info_dict.get('title', 'N/A'))
    print("Uploader:", info_dict.get('uploader', 'N/A'))
    print("Duration (seconds):", info_dict.get('duration', 'N/A'))
    print("View Count:", info_dict.get('view_count', 'N/A'))
