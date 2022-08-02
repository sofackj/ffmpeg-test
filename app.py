import os
from moviepy.editor import *

mp4_path = "/Users/juliensofack-kreutzer/Desktop/schtroumpf_music/mp4/"
mp3_path = "/Users/juliensofack-kreutzer/Desktop/schtroumpf_music/mp3/"

mp4_list = [file for file in os.listdir(mp4_path) if "mp4" in file]

for my_mp4 in mp4_list:
    mp4_file = mp4_path + my_mp4
    mp3_file = mp3_path + my_mp4

    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()