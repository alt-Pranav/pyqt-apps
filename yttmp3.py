import pytube
from moviepy.editor import VideoFileClip

# link= "https://youtu.be/BGIc8kb7dAA" boho days

'''
sample output:
Enter the yt link: https://youtu.be/BGIc8kb7dAA
Downloading video... Please wait.
Downloaded video as tick tick… BOOM!  Andrew Garfield “Boho Days” Official Song Clip  Netflix.mp4
MoviePy - Writing audio in tick tick… BOOM!  Andrew Garfield “Boho Days” Official Song Clip  Netflix.mp3
MoviePy - Done.
Converted video to mp3
'''

link = input("Enter the yt link: ")

def download_video(url):
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(18)
    stream.download()
    return stream.default_filename

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()

print("Downloading video... Please wait.")
try:
    filename = download_video(link)
    print("Downloaded video as " + filename)
except:
    print("Not a valid link..")
try:
    convert_to_mp3(filename)
    print("Converted video to mp3")
except:
    print("Error converting video to mp3")