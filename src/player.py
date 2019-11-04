"""

"""


class Player:
    def __init__(self, name, race, region):
        self.name = name
        self.race = race
        self.region = region


if __name__ == "__main__":
    player1 = Player("Sam", "elf", "north")
    print(player1.name + " is a/an " + player1.race + " from the " + player1.region + " region.")
