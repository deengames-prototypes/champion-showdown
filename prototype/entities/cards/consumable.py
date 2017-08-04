from prototype.entities.cards.card import Card

class Consumable(Card):
    def __init__(self, json):
        super().__init__(json["name"])
        self.effect = json["effect"]