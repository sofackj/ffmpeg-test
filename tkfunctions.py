from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN
from classes import *

def list_of_matches(list_matches: tuple):
    # Window fo matches
    fenetre = Tk()
    fenetre.geometry("1000x850")
    fenetre.resizable(False, False)
    fenetre["bg"] = "white"
    #-----frame examples -----------------------------------------------------------
    my_frame = Frame(fenetre, borderwidth=4, bg="gray")
    my_frame.pack(padx=10, pady=10)
    # List of matches to display in the window
    # Variables for the grid system
    x = 0
    y = 0
    for count, match in enumerate(list_matches):
        if (count+1)%2 == 0:
            match.frame_for_match(my_frame, match.match_id, x, y)
            x += 1
            y = 0
        else:
            match.frame_for_match(my_frame, match.match_id, x, y)
            y += 1
    # Button to destoy the window and continue the program
    button_frame = Frame(fenetre, borderwidth=4, bg="gray")
    button_frame.pack(padx=10, pady=10)
    button = Button(button_frame, text="my button",command=fenetre.destroy)
    button.pack(padx=10, pady=10)
    #-------------------------------------------------------------------------------
    fenetre.mainloop()

if __name__ == '__main__':
    print("\nThis file is not functional... Try with the app.py file\n")