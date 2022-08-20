import os

from random import shuffle

from functions import *
from tkfunctions import *
from pilfunctions import *

from classes import Eligible, Collect_movies

path = "test-app/outputs"
# entry_path = "test-app/entries"
entry_path = "/Users/juliensofack-kreutzer/Desktop/test/new"

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

    phase = 0

    while len(files_list) > 1:
        tournament = create_matches(files_list)
        list_of_matches(tournament)
        setup_score(tournament)
        files_list = qualifications_for_next_phase(path, files_list, phase)
        phase += 1
    
    the_winner = files_list[0]
    final_participant(path, the_winner, phase)
    the_winner.check_participant(the_winner.new_file_path)

if __name__ == '__main__':
    app(8)
    # test()