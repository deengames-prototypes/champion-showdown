from prototype.entities.cards.armour import Armour
from prototype.entities.cards.weapon import Weapon

class Champion:
    def __init__(self, name, health, weapon_data, armour_data):
        self.name = name
        self.current_health = self.total_health = health
        # Make copies so things aren't references of the same objects
        self.weapon = Weapon(weapon_data)
        self.armour = Armour(armour_data)

        # Stuff that's not champion data but player data. Yeah, I know, it's a prototype.
        self.deck = []
        self.hand = []
        self.skill_points = 0
        # hits for one damage each time you take a turn
        self.bleeds_left = 0

    # Player method
    def get_hurt(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            print("{0} dies!".format(self.name))