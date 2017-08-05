import json
import random
import sys

from prototype.entities.champion import Champion
from prototype.entities.cards.action import Action
from prototype.entities.cards.armour import Armour
from prototype.entities.cards.consumable import Consumable
from prototype.entities.cards.skill import Skill
from prototype.entities.cards.weapon import Weapon

class Main:
    # Main entry point!
    def run(self):
        self.load_json_data()
        self.pick_champions()
        self.distribute_cards()

        print("{0} (you) vs. {1}!".format(self.player.name, self.opponent.name))
        self.print_player_stats()

    def load_json_data(self):
        # Load JSON data from files
        with open('data/config.json') as data:
            self.config = json.load(data)

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
        
        # Construct classes
        self.cards = []

        for data in actions:
            self.cards.append(Action(data))

        for data in armour:
            self.cards.append(Armour(data))

        for data in consumables:
            # Consumables show up several times because they're useful.
            # Create copies, not references
            self.cards.append(Consumable(data))
            self.cards.append(Consumable(data))
            self.cards.append(Consumable(data))

        for data in skills:
            self.cards.append(Skill(data))

        for data in weapons:
            self.cards.append(Weapon(data))

        # Populate class instances from said data
        self.champions = []
        for champ_data in champions:
            weapon_data = Weapon.find(weapons, champ_data["weapon"])
            armour_data = Armour.find(armour, champ_data["armour"])
            c = Champion(champ_data["name"], champ_data["health"], weapon_data, armour_data)
            self.champions.append(c)

    def pick_champions(self):
        self.player = self.champions[0]
        index = random.randint(1, len(self.champions) - 1)
        self.opponent = self.champions[index]

    def distribute_cards(self):
        random.shuffle(self.cards)
        self._give_cards_to(self.player)
        self._give_cards_to(self.opponent)        

    def _give_cards_to(self, player):
        while len(player.deck) < self.config["deckSize"]:
            player.deck.append(self.cards.pop())

        while len(player.hand) < self.config["handSize"]:
            player.hand.append(player.deck.pop())

    def print_player_stats(self):
        while self.player.current_health > 0 and self.opponent.current_health > 0:
            Main.print_status_for(self.opponent, self.opponent.name)
            
            Main.print_status_for(self.player, "You")
            print("Your deck has {0} cards left.".format(len(self.player.deck)))
            print("")
            
            print("You have {0} cards in your hand:".format(len(self.player.hand)))            

            i = 1
            for card in self.player.hand:
                print("    {0}) {1}".format(i, card.name))
                i += 1
            
            print("")
            print("Play what card?")

            input = sys.stdin.readline().lower().strip()

            if input == "quit":
                print("Bye!")
                sys.exit(0)
            else:
                try:
                    card_number = int(input) - 1
                    if card_number >= 0 and card_number < len(self.player.hand):
                        card = self.player.hand[card_number]
                        del self.player.hand[card_number]
                        card.apply(self.player, self.opponent)

                        if self.player.bleeds_left > 0:
                            self.player.get_damage(1)
                            print("{0} bleeds for 1 damage!".format(self.player.name))                            
                    else:
                        print("Card number must be from 1-{0}.".format(len(self.player.hand)))
                except ValueError:
                    print("That's not a number, mate. Enter the number of the card to use, or type 'quit' to quit.")            

            print("")

    @staticmethod
    def print_status_for(player, name):
        status = "{3}{4}: {0}/{1} health, {2} sp.".format(
            player.current_health, player.total_health, player.skill_points, name,
            " (bleeding)" if player.bleeds_left > 0 else "")
        if player.weapon != None:
            status = "{0} {1} +{2}/{3}d".format(status, player.weapon.name, player.weapon.damage, player.weapon.durability)
        if player.armour != None:
            status = "{0} {1} +{2}/{3}d".format(status, player.armour.name, player.armour.defense, player.armour.durability)
        
        print(status)

Main().run()