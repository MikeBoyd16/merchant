"""
The Player class
"""
from character import *


class Player(Character):
    def __init__(self, name, race, combat_class):
        super().__init__(name, race, combat_class)

    """
    Adds an item of a specified quantity to the player's inventory
    """
    def add_item(self, item_id, quantity):
        super().add_item(item_id, quantity)
        print("\n" + str(quantity), self.inventory[item_id].name + "(s) added to your inventory")

    """
    Removes an item of a specified quantity from the player's inventory
    """
    def remove_item(self, item_id, quantity):
        if super().remove_item(item_id, quantity) > 0:
            print("\n" + str(quantity), Item(item_id).name + "(s) removed from your inventory")

    """
    Displays item information for every item in a character's inventory
    """
    def display_inventory(self):
        if not super().display_inventory():
            print("\nYour inventory is empty")


if __name__ == "__main__":
    """ PLAYER CREATION"""
    player1 = Player("Sam", "Elf", "Warrior")
    assert player1.name == "Sam"
    assert player1.race == "Elf"
    assert player1.combat_class == "Warrior"
    assert not player1.inventory

    """ INVENTORY MANAGEMENT """
    # Add item to inventory
    player1.add_item("1", 1)
    assert player1.inventory["1"].quantity == 1
    # Remove item from inventory
    player1.remove_item("1", 1)
    assert "1" not in player1.inventory
    # Add multiple items to inventory
    player1.add_item("1", 5)
    assert player1.inventory["1"].quantity == 5
    # Remove multiple items from inventory
    player1.remove_item("1", 5)
    assert "1" not in player1.inventory
    # Remove more items than exist in inventory
    player1.add_item("1", 2)
    assert player1.inventory["1"].quantity == 2
    player1.remove_item("1", 3)
    assert player1.inventory["1"].quantity == 2
    # Clear inventory
    player1.clear_inventory()
    assert not player1.inventory
    # Display empty inventory
    player1.display_inventory()
    # Add item and display inventory
    player1.add_item("1", 1)
    assert player1.inventory["1"].quantity == 1
    player1.display_inventory()
    # Add different item and display inventory with multiple items
    player1.add_item("2", 1)
    assert player1.inventory["2"].quantity == 1
    player1.display_inventory()
