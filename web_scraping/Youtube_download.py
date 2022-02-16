from pytube import YouTube
import os

# This program can download youtube video to mp4 or mp3 
# made by Sansshrek


file_path = str(input("Insert save path file (folder will be created  if it doesn't exist)>>"))
while True:
    link = str(input("Insert youtube link (0 to exit, 1 to change save directory): "))
    if link == "0":
        break
    if link == "1":
        file_path = str(input("Insert save path file (folder will be created  if it doesn't exist)>>"))
        continue
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
        video = yt.streams.filter(file_extension='mp4')  # Filtering Video streams
        video_download = video.first()
        try:
            video_download.download(file_path)  # Trying to download the file
        except:
            print("An Error occurred while downloading the video")
            continue
        print("Download completed in "+file_path)
    else:
        audio = yt.streams.filter(only_audio=True).order_by("abr").last()  # Filtering Audio streams
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