import os

from random import shuffle

from functions import *
from tkfunctions import *
from pilfunctions import *

path = "test-app/outputs"
entry_path = "/Users/juliensofack-kreutzer/Desktop/test/newPics"
# entry_path = "/Users/juliensofack-kreutzer/Desktop/test/newVids"

def test():
    pass

def app(number_of_media):
    # Clean the outputs diretory
    remove_directory_files(path)
    # Add files in the output directory
    move_files(list_files_from_path(participants_list(entry_path, number_of_media)), path)
    # List files in the outputs directory as object
    origin_list = [Participant(file, f"{path}/{file}") for file in os.listdir(path) if '.DS' not in file]
    # Generate id for each object
    generate_id(origin_list)
    # Generate name for each object
    generate_name(origin_list)
    # Duplicate the list to keep a copy in case <- pop will be used
    files_list = origin_list.copy()

    while len(files_list) > 1:
        # Process for winners bracket
        files_list, losers_list = bracket_steps(files_list, path, "Winner Bracket Match")
        while len(losers_list) > 1:
            # Process for losers bracket
            loser_winners_list, losers_list = bracket_steps(losers_list, path, "Loser Bracket Match")
            while len(loser_winners_list) >1:
                # Process for winners in losers bracket
                loser_winners_list, optional_list = bracket_steps(loser_winners_list, path, "Loser Bracket Match")
    
    the_winner = files_list[0]
    final_participant(path, the_winner)
    the_winner.check_participant(the_winner.new_file_path)

if __name__ == '__main__':
    app(4)
    # test()