import random
import json
import os
from dataclasses import dataclass, field
from typing import List, Dict

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
        
@dataclass
class Character:
    name: str
    race: str
    class_type: str
    level: int = 1
    strength: int = 0
    intelligence: int = 0
    wisdom: int = 0
    dexterity: int = 0
    constitution: int = 0
    charisma: int = 0
    hit_points: int = 0
    armor_class: int = 10
    gold: int = 0
    experience: int = 0
    inventory: List[str] = field(default_factory=list)
    equipment: Dict[str, str] = field(default_factory=dict)
    spells: List[str] = field(default_factory=list)
    skills: List[str] = field(default_factory=list)
    
    def add_item(self, item: str):
        self.inventory.append(item)
    
    def remove_item(self, item: str):
        if item in self.inventory:
            self.inventory.remove(item)
    
    def equip_item(self, slot: str, item: str):
        self.equipment[slot] = item
    
    def unequip_item(self, slot: str):
        if slot in self.equipment:
            del self.equipment[slot]
