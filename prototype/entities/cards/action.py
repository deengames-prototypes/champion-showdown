from prototype.entities.cards.card import Card

class Action(Card):
    def __init__(self, json):
        super().__init__(json["name"])
        self.damage_multiplier = json["damageMultiplier"]
        self.hit_probability = json["hitProbability"]