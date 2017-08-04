from prototype.entities.cards.card import Card

class Armour(Card):
    def __init__(self, json):
        super().__init__(json["name"])
        self.durability = json["durability"]
        self.defense = json["defense"]