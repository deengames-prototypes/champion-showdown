from prototype.entities.cards.card import Card

class Weapon(Card):
    def __init__(self, json):
        super().__init__(json["name"])
        self.durability = json["durability"]
        self.attack = json["attack"]