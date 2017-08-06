from prototype.entities.cards.card import Card

import random

class Skill(Card):

    def __init__(self, json):
        super().__init__(json["name"])
        self.effect = json["effect"]
        self.cost = json["cost"]

    # returns false if it couldn't use the skill
    def apply(self, consumer, opponent):
        if consumer.skill_points >= self.cost:
            consumer.skill_points -= self.cost

            index = self.effect.index(" ")
            apply = self.effect[0:index].strip().lower()
            amount = int(self.effect[index:].strip().replace('x', '').replace('+', ''))
            APPLY_EFFECTS[apply](consumer, opponent, self, amount)

            return True
        else:
            print("{3} needs {0} skill points to use {1} (has {2})".format(self.cost, self.name, consumer.skill_points, consumer.name))

            return False

############ SKILL EFFECTS ############
# These are part of the module, not the class.

def hit_opponent(attacker, target, skill_name, times):
    damage = (1 if attacker.weapon is None else attacker.weapon.damage) - (0 if target.armour is None else target.armour.defense)
    damage = damage * times
    if damage > 0:
        target.get_hurt(damage)
        print("{0} uses {1} on {2}! Hit {3} times for {4} total damage!".format(
            attacker.name, skill_name, target.name, times, damage))
    else:
        print("{0} is ineffective against {1}!".format(skill_name, target.name))

def bleed_opponent(target, times):
    target.bleeds_left += times
    print("{0} starts bleeding!".format(target.name))

def heal(me, amount):
    me.current_health += amount
    print("{0} heals for {1}!".format(me.name, amount))

def destroy_opponent_cards(target, n):
    deck = target.deck
    if len(deck) > 0:
        card = random.choice(deck)
        deck.remove(card)
        print("{0}'s '{1}' card burns to ash!".format(target.name, card.name))
    else:
        print("{0} has no cards left in their deck!".format(target.name))
    
APPLY_EFFECTS = {
    'hits': lambda attacker, target, skill, times: hit_opponent(attacker, target, skill.name, times),
    'bleed': lambda attacker, target, skill, times: bleed_opponent(target, times),
    'heal': lambda me, opponent, skill, amount: heal(me, amount),
    'destroy-card': lambda attacker, target, skill, n: destroy_opponent_cards(target, n)
}