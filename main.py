import json

class Main:
    # Main entry point!
    def run(self):
        self.load_json_data()

        print("This is a prototype of the card game battle. BEGIN!")
        print("C: {0}".format(self.champions))
        print("W: {0}".format(self.weapons))
        print("A: {0}".format(self.armour))

    def load_json_data(self):
        with open('data/weapons.json') as data:
            self.weapons = json.load(data)
        
        with open('data/armour.json') as data:
            self.armour = json.load(data)

        with open('data/champions.json') as data:
            self.champions = json.load(data)

Main().run()