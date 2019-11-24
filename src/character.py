"""
The Character class
"""


class Character:
    def __init__(self, name, race, combat_class):
        self.name = name
        self.race = race
        self.combat_class = combat_class
        self.current_location = None
        self.currencies = {}
        self.reputations = {}
        self.inventory = {}
        self.assets = {}


if __name__ == "__main__":
    """ CHARACTER CREATION"""
    character1 = Character("Sam", "Elf", "Warrior")
    assert character1.name == "Sam"
    assert character1.race == "Elf"
    assert character1.combat_class == "Warrior"
    assert not character1.inventory

    """ INVENTORY MANAGEMENT """
