import json

from prototype.entities.champion import Champion

class Main:
    # Main entry point!
    def run(self):
        self.load_json_data()
        print("HELLO YOUTUBES! {0}".format(self.champions))

    def load_json_data(self):
        # Load JSON data from files

        with open('data/weapons.json') as data:
            weapons = json.load(data)
        
        with open('data/armour.json') as data:
            armour = json.load(data)

        with open('data/champions.json') as data:
            champions = json.load(data)

        # Populate class instances from said data
        self.champions = []
        for champ_data in champions:
            c = Champion(champ_data["name"], champ_data["health"], champ_data["weapon"], champ_data["armour"])
            self.champions.append(c)

Main().run()