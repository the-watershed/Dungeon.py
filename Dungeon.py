import random
import json
import os
import time
from decs import Dungeon, Player, Character
from colors import colorize, BLUE, CYAN, GREEN, YELLOW, WHITE, BG_BLUE, RED
from funcs import display_ascii_art



def main():
    dungeon = Dungeon()
    dungeon.create_rooms()
    dungeon.set_starting_room()
    
    player_name = input(colorize("Enter your character's name: ", CYAN))
    dungeon.player = Player(player_name)
    
    print(colorize(f"Welcome, {dungeon.player.name}, to the Great Underground Empire!", YELLOW))
    
    while True:
        print(colorize(f"\nYou are in the {dungeon.current_room.name}", GREEN))
        print(colorize(dungeon.current_room.description, WHITE))
        
        command = input(colorize("What do you want to do? ", CYAN)).lower().split()
        
        if not command:
            continue
        
        if command[0] in ["quit", "exit"]:
            print(colorize("Thanks for playing!", YELLOW))
            break
        elif command[0] == "go":
            if len(command) < 2:
                print(colorize("Go where?", RED))
            else:
                if dungeon.move_player(command[1]):
                    print(colorize(f"You move {command[1]}.", GREEN))
                else:
                    print(colorize("You can't go that way.", RED))
        else:
            print(colorize("I don't understand that command.", RED))

if __name__ == "__main__":
    display_ascii_art()
    print(colorize("Dungeon - Abandon All Hope, Ye Who Enter Here", BLUE, BG_BLUE))
    print(colorize("A Text Adventure of Despair and Discovery", YELLOW, BG_BLUE))
    print()
    main()