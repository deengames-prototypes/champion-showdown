from prototype.entities.cards.card import Card

class Consumable(Card):
    def __init__(self, json):
        super().__init__(json["name"])
        self.effect = json["effect"]

    def apply(self, consumer, opponent):
        index = self.effect.index(" ")
        apply = self.effect[0:index].strip().lower()
        amount = int(self.effect[index:].strip().replace('+', ''))

        if apply == "health":
            consumer.current_health += amount
            print("{0} heals {1} health!".format(consumer.name, amount))
        elif apply == "skillpoints":
            consumer.skill_points += amount
            print("{0} heals {1} skill points!".format(consumer.name, amount))
        else:
            raise NotImplementedError("Not sure how to consume a '{0}' consumable".format(apply))

        return True