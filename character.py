class Character:
    def __init__(self):
        self.name = ""
        self.race = None
        self.character_class = None
        self.stats = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        }
        self.xp = 0
        self.level = 1
        self.inventory = []

    def set_race(self, race):
        self.race = race
        # Apply racial bonuses to stats

    def set_class(self, character_class):
        self.character_class = character_class
        # Apply class-specific modifications
