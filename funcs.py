import time
import os
import random
import json
import curses
from colors import colorize, BLUE, WHITE, GREY, BLACK
import msvcrt
from decs import Player

def display_title_screen():
    ascii_file_path = "./resources/dungeon-ascii.txt"
    if os.path.exists(ascii_file_path):
        with open(ascii_file_path, 'r') as file:
            ascii_art = file.read()
        print(colorize(ascii_art, BLUE, BLACK))
        print(colorize("\nPress any key to continue...", WHITE, BLACK))
        msvcrt.getch()  # Wait for a key press

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colorize("╔════════════════════════════════════╗", WHITE, BLUE))
    print(colorize("║           MAIN MENU                ║", WHITE, BLUE))
    print(colorize("╠════════════════════════════════════╣", WHITE, BLUE))
    print(colorize("║ 1. Load Game                       ║", WHITE, BLUE))
    print(colorize("║ 2. Continue                        ║", WHITE, BLUE))
    print(colorize("║ 3. New Game                        ║", WHITE, BLUE))
    print(colorize("║ 4. Quit                            ║", WHITE, BLUE))
    print(colorize("╚════════════════════════════════════╝", WHITE, BLUE))

def get_menu_choice():
    while True:
        choice = input(colorize("Enter your choice (1-4): ", WHITE, BLUE))
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        print(colorize("Invalid choice. Please try again.", GREY, BLUE))

def handle_menu_choice(choice):
    if choice == 1:
        print(colorize("Loading game...", WHITE, BLUE))
        # Implement load game functionality
    elif choice == 2:
        print(colorize("Continuing game...", WHITE, BLUE))
        # Implement continue game functionality
    elif choice == 3:
        print(colorize("Starting new game...", WHITE, BLUE))
        return "new_game"
    elif choice == 4:
        print(colorize("Thanks for playing!", WHITE, BLUE))
        exit()

def main_menu():
    display_title_screen()
    while True:
        display_menu()
        choice = get_menu_choice()
        result = handle_menu_choice(choice)
        if result == "new_game":
            return

def roll_dice(num_dice, num_sides):
    return sum(random.randint(1, num_sides) for _ in range(num_dice))
# Add other functions here as needed

from character import Character
import json

def create_character():
    character = Character()
    
    character.name = input("Enter your character's name: ")
    
    races = load_races()
    selected_race = display_race_selection(races)
    character.set_race(selected_race)
    
    classes = load_classes()
    selected_class = display_class_selection(classes, selected_race['name'])
    character.set_class(selected_class)
    
    return character

def load_races():
    with open('./resources/races.json', 'r') as f:
        return json.load(f)

def display_race_selection(races):
    print("Available races:")
    def display_race_selection(races):
        print("Available races:")
        for race in races['races']:
            print(f"{race['id']}. {race['name']}")
    
        while True:
            choice = input("Choose a race (enter the number or name): ")
            try:
                choice = int(choice)
                selected_race = next((race for race in races['races'] if race['id'] == choice), None)
            except ValueError:
                selected_race = next((race for race in races['races'] if race['name'].lower() == choice.lower()), None)
        
            if selected_race:
                return selected_race
            else:
                print("Invalid choice. Please try again.")

    def load_classes():
        with open('./resources/classes.json', 'r') as f:
            return json.load(f)

    def display_class_selection(classes, race_name):
        race_name_lower = race_name.lower()
        available_classes = next((classes[key] for key in classes if key.lower() == race_name_lower), None)
    
        if available_classes is None:
            print(f"No classes found for {race_name}. Available races: {', '.join(classes.keys())}")
            return None

        print(f"Available classes for {race_name}:")
        for i, class_name in enumerate(available_classes, 1):
            print(f"{i}. {class_name}")
    
        while True:
            choice = input("Choose a class (enter the number or name): ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(available_classes):
                    return available_classes[choice - 1]
            except ValueError:
                selected_class = next((c for c in available_classes if c.lower() == choice.lower()), None)
                if selected_class:
                    return selected_class
        
            print("Invalid choice. Please try again.")        except ValueError:
            print("Please enter a valid number.")
