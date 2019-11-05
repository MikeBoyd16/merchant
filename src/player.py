"""

"""
from item import *


class Player:
    def __init__(self, name, race, region):
        self.name = name
        self.race = race
        self.region = region
        self.inventory = {}


if __name__ == "__main__":
    player1 = Player("Sam", "elf", "north")
    print(player1.name + " is a/an " + player1.race + " from the " + player1.region + " region.")

    item1 = Item("1")
    player1.inventory[item1.id] = item1
    print(player1.inventory[item1.id].name + " is a " + player1.inventory[item1.id].type + " that costs " +
          str(player1.inventory[item1.id].base_value) + " gold and " + player1.inventory[item1.id].description)
