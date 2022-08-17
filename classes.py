from cgitb import grey
import subprocess

from tkinter import *

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
        self.score = 0
        self.id = None
    
    def check_participant(self, path):
    # Display participants through the subprocess module
        my_path = (subprocess.run(["pwd"], capture_output=True, text=True))
        subprocess.run(["open", f"{my_path.stdout[:-1]}/{path}"])
    
    def frame_participant(self, window, frame_side):
        # Frame to includes the widgets of the participant
        fr = Frame(window, borderwidth=4)
        fr.pack(padx=20, pady=20, side=frame_side)
        return fr
    
    def label_participant(self, window):
        lb = Label(window, text=self.filename)
        lb.pack()
        return lb

    def radiobutton(self, window, result):
        # Radiobutton to choose the winner
        rb = Radiobutton(window, text=self.filename, variable=result, value=self.id)
        rb.pack()
        return rb
    
    def display_picture(self, window):
        # Button to display picture
        my_button =  Button(window, text="show", command=lambda : self.check_participant(self.file_path))
        my_button.pack()
        return my_button

class Match:
    """
    Match of the tournament
    """
    def __init__(self, participants, match_id):
        self.participants = participants
        self.match_id = match_id
        self.winner = None
    
    def frame_for_match(self, window, match_id, x, y):
        first, second = self.participants
        # Main frame
        my_frame = Frame(window, borderwidth=4)
        my_frame.grid(row=x, column=y, padx=20, pady=20)
        # Match label
        my_label = Label(my_frame, text=f"Match {match_id}\n{first.filename} VS {second.filename}")
        my_label.pack()

        # Pick up result of the match in self.winner with radiobuttons
        self.winner = StringVar()

        # Left frame
        my_first_frame = first.frame_participant(my_frame, LEFT)
        # first_label = first.label_participant(my_first_frame)
        first_rb = first.radiobutton(my_first_frame, self.winner)
        first_button = first.display_picture(my_first_frame)

        # Right frame
        my_second_frame = second.frame_participant(my_frame, RIGHT)
        # second_label = second.label_participant(my_second_frame)
        second_rb = second.radiobutton(my_second_frame, self.winner)
        second_button = second.display_picture(my_second_frame)
        return my_frame

class Window(Tk):
    def __init__(self):
        print("hello world")

if __name__ == '__main__':
    print("\nThis file is not functional... Try with the app.py file\n")