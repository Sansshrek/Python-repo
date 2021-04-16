from pytube import YouTube
import os

# This program can download youtube video to mp4 or mp3

while True:
    link = str(input("Insert youtube link (0 to exit): "))
    if link == "0":
        break
    try:
        yt = YouTube(link)  # Creating object YouTube with link
    except:
        print("Connection Error")
        continue
    while True:
        choice = int(input("Want to download Video(1) or Mp3(2)?: "))
        if choice == 1 or choice == 2:
            break
    if choice == 1:
        video = yt.streams.filter('mp4')  # Filtering Video streams
        video_download = yt.streams.first()
        file_path = str(input("Insert save path file (folder will be created  if it doesn't exist)>>"))
        try:
            video_download.download(file_path)  # Trying to download the file
        except:
            print("An Error occurred while downloading the video")
            continue
        print("Download completed in "+file_path)
    else:
        audio = yt.streams.filter(only_audio=True).first()  # Filtering Audio streams
        file_path = str(input("Insert save path file (folder will be created  if it doesn't exist)>>"))
        try:
            audio_download = audio.download(file_path)  # Trying to download the file
        except:
            print("An Error occurred while downloading the audio")
            continue
        base, ext = os.path.splitext(audio_download)
        audio_file = base + ".mp3"
        try:
            os.rename(audio_download, audio_file)  # Changing file with mp3
        except:
            print("File already exist")
            continue
        print("Download completed in "+file_path)