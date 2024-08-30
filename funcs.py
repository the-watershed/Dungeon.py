import time
import os
import random
from colors import colorize, YELLOW

def display_ascii_art():
    ascii_file_path = "./resources/dungeon-ascii.txt"
    if os.path.exists(ascii_file_path):
        with open(ascii_file_path, 'r') as file:
            ascii_art = file.read()
        print(colorize(ascii_art, YELLOW))
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

def roll_dice(num_dice, num_sides):
    return sum(random.randint(1, num_sides) for _ in range(num_dice))

# Add other functions here as needed