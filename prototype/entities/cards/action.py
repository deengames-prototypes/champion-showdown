from prototype.entities.cards.card import Card

import random

class Action(Card):
    def __init__(self, json):
        super().__init__(json["name"])
        self.damage_multiplier = json["damageMultiplier"]
        self.hit_probability = json["hitProbability"]

    def apply(self, consumer, opponent):
        if random.randint(1, 100) <= self.hit_probability:
            total_damage = (consumer.weapon.damage or 1) * self.damage_multiplier
            print("{0} {1}s {2} for {3} damage!".format(consumer.name, self.name, opponent.name, total_damage))            
            opponent.get_hurt(total_damage)
        else:
            print("{0} misses his {1}!".format(consumer.name, self.name))
        
        return True