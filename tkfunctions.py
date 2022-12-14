from tkinter import *
from classes import *
from tkVideoPlayer import TkinterVideo

def list_of_matches(list_matches: tuple):
    # Window fo matches
    fenetre = Tk()
    fenetre.geometry("1000x600+50+50")
    fenetre.resizable(False, False)
    fenetre["bg"] = "white"
    #-----frame examples -----------------------------------------------------------
    # Setup the scrollbar
    # Setuo canvas, scollbar and frame
    my_canvas = Canvas(fenetre)
    my_frame = Frame(my_canvas, bg="blue")
    my_scrollbar = Scrollbar(fenetre, width=40, orient="vertical", command=my_canvas.yview)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_frame.pack()
    my_scrollbar.pack(side="right", fill="y")
    my_canvas.pack(side="left", fill="both", expand=True)
    # Create windows via the canvas corresponding to the frame
    my_canvas.create_window((0,0), window=my_frame, anchor="nw")
    # Bind the scrollbar to the canvas containing the frame
    my_frame.bind("<Configure>", lambda event, canvas=my_canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    # List of matches to display in the window
    for count, match in enumerate(list_matches):

        a, b = match.participants
        main_frame, my_first_frame, my_second_frame = match.frame_for_match(my_frame, match.match_id)
        # We consider all videos will get the mp4 extension
        if "mp4" in a.filename:
            a.display_button(my_first_frame)
            b.display_button(my_second_frame)
            a.display_video(my_first_frame)
            b.display_video(my_second_frame)
        # Everything elese will be image format
        else:
            a.tk_image = open_image_and_resize(a.file_path, 200)
            b.tk_image = open_image_and_resize(b.file_path, 200)
            a.display_picture(my_first_frame, a.tk_image)
            b.display_picture(my_second_frame, b.tk_image)

    button_frame = Frame(fenetre, borderwidth=4, bg="gray")
    button_frame.pack(side=BOTTOM, padx=10, pady=10)

    def stop_and_quit():
        for i in list_matches:
            j,k = i.participants
            if ".mp4" in j.filename:
                j.test.stop()
                k.test.stop()
        fenetre.destroy()

    button = Button(button_frame, text="Next Phase",command=stop_and_quit)
    button.pack(padx=10, pady=10)
    #-------------------------------------------------------------------------------
    fenetre.mainloop()

if __name__ == '__main__':
    print("\nThis file is not functional... Try with the app.py file\n")