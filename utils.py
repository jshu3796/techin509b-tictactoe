# utils.py

import csv
import os

DATABASE_FILE = 'logs/game_results.csv'

def write_to_csv(winner, moves, first_player_moves):
    if not os.path.isfile(DATABASE_FILE):
        with open(DATABASE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Winner', 'Moves', 'First_Player_Moves'])

    with open(DATABASE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([winner, moves, first_player_moves])
