import random
import json
import os

class Dungeon:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.player = None

    def create_rooms(self):
        # Load rooms from JSON file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, 'resources', 'rooms.json')
        
        with open(json_path, 'r') as f:
            rooms_data = json.load(f)

        # Create Room objects
        for room_name, room_info in rooms_data.items():
            self.rooms[room_name] = Room(room_name, room_info['description'])

        # Connect rooms
        for room_name, room_info in rooms_data.items():
            for direction, connected_room in room_info['exits'].items():
                self.rooms[room_name].connect_room(direction, self.rooms[connected_room])

    def set_starting_room(self):
        self.current_room = self.rooms["Entrance"]

    def move_player(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            return True
        return False

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.enemies = []
        self.is_locked = False
        self.locked_by = None
        self.is_cleared = False
        self.is_cleared_by = None
        self.is_cleared_by_enemy = False
        self.is_cleared_by_player = False
        self.is_cleared_by_item = False
        self.is_cleared_by_key = False

    def connect_room(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 20
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def roll_dice(num_dice, sides):
    return sum(random.randint(1, sides) for _ in range(num_dice))
