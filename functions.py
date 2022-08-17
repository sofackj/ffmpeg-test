import os

from random import randint, shuffle, choice
from shutil import move, copy

from classes import Match, Participant

#================================ Entries setup ================================

def list_files_from_path(path: str):
    # Create a list of Participants from a directory
    final_list = [Participant(file, f"{path}/{file}") for file in os.listdir(path) if '.DS' not in file]
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
    for participant in start_list:
        while True:
            id = randint(101, 501)
            if str(id) not in [participant.id for participant in start_list]:
                participant.id = str(id)
                break

def remove_directory_files(directory_path):
    # Be sure that no files are present
    for file in os.listdir(directory_path):
        os.remove(f"{directory_path}/{file}")

#=========================== Setup matches and scores afterwards ===========================

def create_matches(start_list: list):
    start_list_copy = start_list.copy()
    final_list = []
    if len(start_list_copy)%2 == 0:
        for match_nb in range(int(len(start_list_copy)/2)):
            final_list.append(Match((start_list_copy.pop(0), start_list_copy.pop(0)), match_nb+1))
        return tuple(final_list)

def setup_score(matches_list: tuple):
    for match in matches_list:
        for participant in match.participants:
            if match.winner.get() == participant.id:
                participant.score += 1

#=========================== qualifications_for_next_phase ===========================

def highest_value(start_list: list):
    highest_value = 0
    for participant in start_list:
        if participant.score > highest_value:
            highest_value = participant.score
    return highest_value

def qualifications_for_next_phase(path: str, start_list: list, tournament_phase: int):
    final_list = []
    qualification_factor = highest_value(start_list)
    for participant in start_list:
        if participant.score == qualification_factor:
            final_list.append(participant)
        else:
            participant.new_file_path = f"{path}/{str(tournament_phase)}_{participant.filename}"
            move(participant.file_path, participant.new_file_path)
    return final_list

#====================================================================================

def final_participant(path: str, participant: object, tournament_phase: int):
    participant.new_file_path = f"{path}/{str(tournament_phase)}_{participant.filename}"
    move(participant.file_path, participant.new_file_path)
                
if __name__ == '__main__':
    print("\nThis file is not functional... Try with the app.py file\n")