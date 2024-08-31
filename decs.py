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
        rooms_file_path = os.path.join('resources', 'rooms.json')
        with open(rooms_file_path, 'r') as f:
            rooms_data = json.load(f)
        
        for room_name, room_info in rooms_data.items():
            new_room = Room(room_name, room_info['description'])
            if 'items' in room_info:
                for item in room_info['items']:
                    new_room.add_item(item)
            self.rooms[room_name] = new_room
        
        for room_name, room_info in rooms_data.items():
            for direction, connected_room in room_info['exits'].items():
                self.rooms[room_name].exits[direction] = self.rooms[connected_room]    
                
    def set_starting_room(self):
        self.current_room = self.rooms['Forest Clearing']

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
        self.inventory = []  # New attribute for room inventory

    def connect_room(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False

    def get_items(self):
        return ", ".join(self.inventory) if self.inventory else "No items here."

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
