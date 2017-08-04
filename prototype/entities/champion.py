class Champion:
    def __init__(self, name, health, weapon, armour):
        self.name = name
        self.current_health = self.total_health = health
        self.weapon = weapon
        self.armour = armour

        # Stuff that's not champion data but player data. Yeah, I know, it's a prototype.
        self.deck = []
        self.hand = []
        self.skill_points = 0 

    def __repr__(self):
        return "{0} ({1}/{2}) - {3} and {4}".format(self.name, self.current_health, self.total_health, self.weapon, self.armour)