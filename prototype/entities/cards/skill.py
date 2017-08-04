from prototype.entities.cards.card import Card

class Skill(Card):
    def __init__(self, json):
        super().__init__(json["name"])
        self.effect = json["effect"]
        self.cost = json["cost"]