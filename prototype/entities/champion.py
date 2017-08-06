from prototype.entities.cards.armour import Armour
from prototype.entities.cards.weapon import Weapon

class Champion:
    def __init__(self, name, health, weapon_data, armour_data):
        self.name = name
        self.current_health = self.total_health = health
        # Make copies so things aren't references of the same objects
        self.weapon = Weapon(weapon_data)
        self.armour = Armour(armour_data)

        # Non-prototype stuff
        self.deck = []
        self.hand = []
        self.skill_points = 0
        # hits for one damage each time you take a turn
        self.bleeds_left = 0

    def get_hurt(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            print("{0} dies!".format(self.name))
        if self.armour != None:
            self.armour.durability -= 1
            if self.armour.durability <= 0:
                print("{0}'s {1} is destroyed!".format(self.name, self.armour.name))
                self.armour = None

    def attacks(self):
        if self.weapon != None:
            self.weapon.durability -= 1
            if self.weapon.durability <= 0:
                print("{0}'s {1} breaks!".format(self.name, self.weapon.name))
                self.weapon = None

    def heal(self, amount):
        amount = min(amount, self.total_health - self.current_health)
        self.current_health += amount
        return amount