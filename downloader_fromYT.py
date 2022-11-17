# dependencies must be installed to run this program
from moviepy.editor import *
from pytube import YouTube

"""
this program will ask for educational purposes only, it will download a video with the highest resolution posible
or audio format and it also could be converted into mp3, because the default format is mp4

"""

link = input("Please provide the link from Youtube:\n")
choice = input("do you want to extract video or audio?\n").lower()

#evaluating the answers
if not (choice == "audio" or choice =="video"):
    exit
else:
    if choice == "audio":
        format = input("Do you want your audio in mp4 or mp3?\n").lower()
    if not (format == "mp4" or format =="mp3"):
        exit

#funtion for downloading the video        
def get_video(link = link):
    
    try:
        url = YouTube(link) #This captures the link(url) and locates it from YouTube.
        video = url.streams.get_highest_resolution() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
        video.download() # This is the method with the instruction to download the video.
        print('Download Completed!')


    except:
        print("Error downloading the file")


#function getting the audio in mp4 format
def extract_audio(link = link):
    
    try:
        url = YouTube(link)
        #print(video.streams.filter(only_audio=True))
        # filtering the audio. File extension can be mp4/webm
        # You can see all the available streams by print(video.streams)
        audio = url.streams.filter(only_audio=True, file_extension='mp4').first()
        audio.download(filename= "output_audio.mp4")
        print('Download Completed!')

    except:
        print("Connection Error")  # to handle exception

#function converting the mp4 file to mp3 file
def mp4_to_mp3(mp4 = "output_audio.mp4", mp3 = "output_audio.mp3"):
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close()
    print('Conversion Completed!')

#calling the needed functions to process the request

if choice == "video":
    get_video()
elif choice == "audio" and format == "mp4":
    extract_audio()
elif choice == "audio" and format == "mp3":
    extract_audio()
    mp4_to_mp3()
else:
    print("check your inputs")