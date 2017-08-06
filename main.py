from enum import Enum
import json
import random
import sys
import time

from prototype.entities.champion import Champion
from prototype.entities.cards.action import Action
from prototype.entities.cards.armour import Armour
from prototype.entities.cards.consumable import Consumable
from prototype.entities.cards.skill import Skill
from prototype.entities.cards.weapon import Weapon

class WhoseTurn(Enum):
    PLAYER = 1
    AI = 2

class Main:
    # Main entry point!
    def run(self):
        self.whoseTurn = WhoseTurn.PLAYER

        self.load_json_data()
        self.pick_champions()
        self.distribute_cards()

        print("")
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
            # Consumables show up several times because they're basic attacks.
            self.cards.append(Action(data))
            self.cards.append(Action(data))
            self.cards.append(Action(data))
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
            self._draw_cards(player)

    def print_player_stats(self):
        while self.player.current_health > 0 and self.opponent.current_health > 0:
            if self.whoseTurn == WhoseTurn.PLAYER:
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
                elif input == "draw":
                    self._get_card(self.player)                                
                    self.whoseTurn = WhoseTurn.AI
                    time.sleep(0.5)
                else:
                    try:
                        card_number = int(input) - 1
                        if card_number >= 0 and card_number < len(self.player.hand):
                            card = self.player.hand[card_number]
                            took_action = Main.process_turn(self.player, self.opponent, card)

                            if took_action:
                                self._draw_cards(self.player)                                
                                self.whoseTurn = WhoseTurn.AI
                                time.sleep(0.5)
                        else:
                            print("Card number must be from 1-{0}.".format(len(self.player.hand)))
                    except ValueError:
                        print("That's not a number, mate. Enter the number of the card to use, or type 'quit' to quit.")            
            else:
                self._draw_cards(self.opponent)                
                card = random.choice(self.opponent.hand)
                Main.process_turn(self.opponent, self.player, card)
                self.whoseTurn = WhoseTurn.PLAYER
                time.sleep(0.5)                

            print("")
    
    def _draw_cards(self, champion):
        while len(champion.deck) > 0 and len(champion.hand) < self.config["handSize"]:
            self._get_card(champion)

    def _get_card(self, champion):
        if len(champion.deck) > 0:
            card = champion.deck.pop()
            champion.hand.append(card)
            if (champion == self.player):
                print("You draw a {0} card".format(card.name))
            else:
                print("{0} draws a card".format(champion.name))
        else:
            print("{0}'s deck is empty!".format(champion.name))

    @staticmethod
    def process_turn(player, opponent, card):
        took_action = card.apply(player, opponent)

        if took_action:
            player.hand.remove(card)
            if player.bleeds_left > 0:
                player.bleeds_left -= 1
                player.get_hurt(1)
                print("{0} bleeds for 1 damage!".format(player.name))

        return took_action

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