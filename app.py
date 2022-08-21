import os

from random import shuffle

from functions import *
from tkfunctions import *
from pilfunctions import *

from classes import Eligible, Collect_movies

path = "test-app/outputs"
entry_path = "test-app/entries"
# entry_path = "/Users/juliensofack-kreutzer/Desktop/test/new"

def test():
    my_string = "hello"
    hello = my_string.split("_")
    hello.insert(-1, "a")
    hello = "_".join(hello)
    print(hello)

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
        tournament = create_matches(files_list, "Winner Bracket Match")
        list_of_matches(tournament)
        setup_score(tournament)
        files_list, losers_list = qualifications_for_next_phase(path, files_list)
        while len(losers_list) > 1:
            tournament = create_matches(losers_list, "Loser Bracket Match")
            list_of_matches(tournament)
            setup_score(tournament)
            loser_winners_list, losers_list = qualifications_for_next_phase(path, losers_list)
            while len(loser_winners_list) >1:
                tournament = create_matches(loser_winners_list, "Loser Bracket Match")
                list_of_matches(tournament)
                setup_score(tournament)
                loser_winners_list, optional_list = qualifications_for_next_phase(path, loser_winners_list)
    
    the_winner = files_list[0]
    final_participant(path, the_winner)
    the_winner.check_participant(the_winner.new_file_path)

if __name__ == '__main__':
    app(16)
    # test()