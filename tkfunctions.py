from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN
from classes import *

def list_of_matches(list_matches: tuple):
    # Window fo matches
    fenetre = Tk()
    fenetre.geometry("600x600")
    fenetre.resizable(False, False)
    fenetre["bg"] = "white"
    #-----frame examples -----------------------------------------------------------
    # Setup the scrollbar

    my_canvas = Canvas(fenetre)
    my_frame = Frame(my_canvas)
    my_scrollbar = Scrollbar(fenetre, width=40, orient="vertical", command=my_canvas.yview)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)

    my_frame.grid(column=2)
    my_scrollbar.pack(side="right", fill="y")
    my_canvas.pack(side="left", fill="both", expand=True)

    my_canvas.create_window((0,0), window=my_frame, anchor="nw")

    my_frame.bind("<Configure>", lambda event, canvas=my_canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    # List of matches to display in the window
    for count, match in enumerate(list_matches):
        match.frame_for_match(my_frame, match.match_id)

    button_frame = Frame(fenetre, borderwidth=4, bg="gray")
    button_frame.pack(side=BOTTOM, padx=10, pady=10)
    button = Button(button_frame, text="my button",command=fenetre.destroy)
    button.pack(padx=10, pady=10)
    #-------------------------------------------------------------------------------
    fenetre.mainloop()

if __name__ == '__main__':
    print("\nThis file is not functional... Try with the app.py file\n")