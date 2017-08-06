from prototype.entities.cards.card import Card

class Armour(Card):
    def __init__(self, json):
        super().__init__(json["name"])
        self.durability = json["durability"]
        self.defense = json["defense"]

    def apply(self, consumer, opponent):
        consumer.armour =  self
        print("{0} puts on the {1}".format(consumer.name, self.name))
        return True

    @staticmethod
    def find(armours, name):
        for armour in armours:
            if armour["name"].lower() == name.lower():
                return armour

        return None