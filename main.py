import json
import random

from prototype.entities.champion import Champion
from prototype.entities.cards.card import Card

class Main:
    # Main entry point!
    def run(self):
        self.load_json_data()
        self.pick_champions()
        print("{0} vs. {1}!".format(self.player.name, self.opponent.name))

    def load_json_data(self):
        # Load JSON data from files

       
        with open('data/actions.json') as data:
            actions = json.load(data)

        with open('data/armour.json') as data:
            armour = json.load(data)

        with open('data/champions.json') as data:
            champions = json.load(data)
        
        with open('data/consumables.json') as data:
            consumables = json.load(data)

        with open('data/skills.json') as data:
            skills = json.load(data)
        
        with open('data/weapons.json') as data:
            weapons = json.load(data)
        
        # Populate class instances from said data
        self.champions = []
        for champ_data in champions:
            c = Champion(champ_data["name"], champ_data["health"], champ_data["weapon"], champ_data["armour"])
            self.champions.append(c)

        self.cards = []
        # Consumables show up several times because they're useful.
        for item in actions + armour + consumables + consumables + consumables + skills + weapons:
            c = Card(item["name"])
            self.cards.append(c)

        print(self.cards)

    def pick_champions(self):
        self.player = self.champions[0]
        index = random.randint(1, len(self.champions) - 1)
        self.opponent = self.champions[index]

Main().run()