from prototype.entities.cards.card import Card

class Weapon(Card):
    def __init__(self, json):
        super().__init__(json["name"])
        self.durability = json["durability"]
        self.damage = json["damage"]

    def apply(self, consumer, opponent):
        consumer.weapon =  self
        return True

    @staticmethod
    def find(weapons, name):
        for weapon in weapons:
            if weapon["name"].lower() == name.lower():
                return weapon

        return None