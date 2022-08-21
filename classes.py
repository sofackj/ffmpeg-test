import os
import subprocess

from tkinter import *
from pilfunctions import *
from tkVideoPlayer import TkinterVideo

class Eligible:
    def __init__(self, file_path):
        self.file_path = file_path
        self.filename = self.file_path.split("/")[-1]
        if len(self.filename.split("_")) > 1:
            self.serie = self.filename.split("_")[-2]

class Serie:
    def __init__(self, serie):
        self.id = serie
        self.elements_list = []

class Collect_movies:
    def __init__(self, path):
        self.elements_list = [Eligible(f"{path}/{video}") for video in os.listdir(path) if ".DS_" not in video]
        self.series_list = [Serie(serie) for serie in set([movie.serie for movie in self.elements_list])]

class Participant:
    """
    Participant for the tournament
    """
    def __init__(self, filename, filepath):
        self.filename = filename
        self.file_path = filepath
        self.new_file_path = None
        self.extension = self.filename.split(".")[-1]
        self.participant_name = None
        self.tk_image = None
        self.score = 0
        self.id = None
        self.test = None
    
    def check_participant(self, path):
    # Display participants through the subprocess module
        my_path = (subprocess.run(["pwd"], capture_output=True, text=True))
        subprocess.run(["open", f"{my_path.stdout[:-1]}/{path}"])
    
    def frame_participant(self, window, frame_side):
        # Frame to includes the widgets of the participant
        fr = Frame(window, borderwidth=4, bg="orange")
        fr.pack(padx=20, pady=20, side=frame_side)
        return fr
    
    def label_participant(self, window):
        lb = Label(window, text=self.participant_name)
        lb.pack()
        return lb

    def radiobutton(self, window, result):
        # Radiobutton to choose the winner
        rb = Radiobutton(window, variable=result, value=self.id)
        rb.pack(pady=10)
        return rb
    
    def display_button(self, window):
        # Button to display picture
        my_button =  Button(window, text="Open", command=lambda : self.check_participant(self.file_path))
        my_button.pack()
        return my_button
    
    def display_picture(self, window, img):
        # Button to display picture
        my_button =  Button(window, image=img, command=lambda : self.check_participant(self.file_path))
        my_button.pack()
        return my_button
    
    def display_video(self, window):
        # Display videos
        self.test = TkinterVideo(master=window, scaled=True)
        self.test.load(self.file_path)
        self.test.pack(padx=10, pady=10, expand=True, fill="both")
        self.test.play()
        def play_file():
             self.test.play()
        my_button = Button(window, text="Play", command=play_file)
        my_button.pack()

class Match:
    """
    Match of the tournament
    """
    def __init__(self, participants, match_id, win_lose_bracket):
        self.participants = participants
        self.match_id = match_id
        self.win_lose_bracket = win_lose_bracket
        self.winner = None
    
    def frame_for_match(self, window, match_id):
        first, second = self.participants
        # Main frame
        my_frame = Frame(window, borderwidth=4, bg="red")
        my_frame.pack(padx=5, pady=5)
        # my_frame.grid(row=x, column=y, padx=20, pady=20)
        # Match label
        my_label = Label(my_frame, text=f"{self.win_lose_bracket} {match_id}")
        my_label.pack()

        # Pick up result of the match in self.winner with radiobuttons
        self.winner = StringVar()

        # Left frame
        my_first_frame = first.frame_participant(my_frame, LEFT)
        first_lb = first.label_participant(my_first_frame)
        first_rb = first.radiobutton(my_first_frame, self.winner)

        # Right frame
        my_second_frame = second.frame_participant(my_frame, RIGHT)
        second_lb = second.label_participant(my_second_frame)
        second_rb = second.radiobutton(my_second_frame, self.winner)
        
        return my_frame, my_first_frame, my_second_frame

if __name__ == '__main__':
    print("\nThis file is not functional... Try with the app.py file\n")