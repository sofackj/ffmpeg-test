import os

from random import shuffle
from shutil import move, copy

from classes import Match, Participant, Eligible, Collect_movies
from tkfunctions import *

#================================ Entries setup ================================
def check_for_series(path: str):
    for element in os.listdir(path):
        if "_dia_lookfor" in element:
            return True
        else:
            return False

def setup_entries(series_list, movies_list):
    for serie in series_list:
        for movie in movies_list:
            if serie.id == movie.serie:
                serie.elements_list.append(movie)

def collect_entries(series_list, movies_nb):
    my_list = []
    n = 0
    while len(my_list) < movies_nb:
        shuffle(series_list[n].elements_list)
        my_list.append(series_list[n].elements_list.pop())
        if len(series_list[n].elements_list) == 0:
            series_list.pop(n)
        else:
            n += 1
    return my_list

def participants_list(entry_path, elements_nb):
    # Check if series or not
    if check_for_series(entry_path):
        # Collectig objecs
        my_collect = Collect_movies(entry_path)
        # Catch movies by serie object
        setup_entries(my_collect.series_list, my_collect.elements_list)
        # Choose movies
        elements_list = collect_entries(my_collect.series_list, elements_nb)
    else:
        # If no series just catch elements
        elements_list = [Eligible(f"{entry_path}/{element}") for element in os.listdir(entry_path) if ".DS_" not in element][:elements_nb]
        # Randomize the list
        shuffle(elements_list)
    # Return elements
    return elements_list

#================================ Output setup ================================

def list_files_from_path(list_of_participants: list):
    # Create a list of Participants from a directory
    final_list = [Participant(participant.filename, participant.file_path) for participant in list_of_participants]
    shuffle(final_list)
    return final_list

def random_items_list(start_list: list, element_nb: int):
    if element_nb > len(start_list):
        print("The list of items is not enough... Reconsider the number of random elements")
        return False
    else:
        return start_list[:element_nb]

def move_files(start_list: list, dest_path: str):
    n = 1
    for file in start_list:
        # New name for the file
        file.participant_file = f"Participant-{n}"
        file.participant_name = " ".join(file.participant_file.split("-"))
        # New destination -> new file path
        file.new_file_path = f"{dest_path}/{file.participant_file}.{file.extension}"
        copy(file.file_path, file.new_file_path)
        n += 1
    return start_list

#================================ Essentials ================================

def generate_id(start_list: list):
    # Generate IDs for each media
    for count, participant in enumerate(start_list):
        participant.id = str(200+count)

def generate_name(start_list: list):
    for participant in start_list:
        filename = participant.filename
        participant.participant_name = " ".join(filename.split(".")[0].split("-"))

def remove_directory_files(directory_path):
    # Be sure that no files are present
    for file in os.listdir(directory_path):
        os.remove(f"{directory_path}/{file}")

#=========================== Setup matches and scores afterwards ===========================

def create_matches(start_list: list, win_lose_bracket: str):
    start_list_copy = start_list.copy()
    final_list = []
    if len(start_list_copy)%2 == 0:
        for match_nb in range(int(len(start_list_copy)/2)):
            final_list.append(Match((start_list_copy.pop(0), start_list_copy.pop(0)), match_nb+1, win_lose_bracket))
        return tuple(final_list)

def setup_score(matches_list: tuple):
    for match in matches_list:
        for participant in match.participants:
            if match.winner.get() == participant.id:
                participant.score += 1

#=========================== qualifications_for_next_phase ===========================

def add_prefix(my_string: str, prefix: str):
    new_name = my_string.split("_")
    new_name.insert(-1, prefix)
    new_name = "_".join(new_name)
    return new_name

def highest_value(start_list: list):
    highest_value = 0
    for participant in start_list:
        if participant.score > highest_value:
            highest_value = participant.score
    return highest_value

def qualifications_for_next_phase(path: str, start_list: list):
    final_list = []
    losers_list = []
    qualification_factor = highest_value(start_list)
    for participant in start_list:
        if participant.score == qualification_factor:
            final_list.append(participant)
        else:
            losers_list.append(participant)
            new_file_name = add_prefix(participant.filename, str(participant.score))
            new_file_path = f"{path}/{new_file_name}"
            move(participant.file_path, new_file_path)
            participant.filename = new_file_name
            participant.file_path = new_file_path
    return final_list, losers_list
#=========================== Losers Bracket ===========================

def bracket_steps(start_list: list, path, bracket_type: str):
    tournament = create_matches(start_list, bracket_type)
    list_of_matches(tournament)
    setup_score(tournament)
    start_list, losers_list = qualifications_for_next_phase(path, start_list)
    return start_list, losers_list
#====================================================================================
def final_participant(path: str, participant: object):
    new_file_name = add_prefix(participant.filename, str(participant.score))
    new_file_path = f"{path}/{new_file_name}"
    move(participant.file_path, new_file_path)
    participant.filename = new_file_name
    participant.file_path = new_file_path
                
if __name__ == '__main__':
    print("\nThis file is not functional... Try with the app.py file\n")