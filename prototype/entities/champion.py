class Champion:
    def __init__(self, name, health, weapon, armour):
        self.name = name
        self.current_health = self.total_health = health
        self.weapon = weapon
        self.armour = armour

    def __repr__(self):
        return "{0} ({1}/{2}) - {3} and {4}".format(self.name, self.current_health, self.total_health, self.weapon, self.armour)