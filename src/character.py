"""
The Character class
"""
from item import *


class Character:
    def __init__(self, name, race, combat_class):
        self.name = name
        self.race = race
        self.combat_class = combat_class
        self.inventory = {}

    """
    Adds an item of a specified quantity to a character's inventory
    """
    def add_item(self, item_id, quantity):
        if item_id in self.inventory:
            self.inventory[item_id].quantity += quantity
        else:
            self.inventory[item_id] = Item(item_id)
            self.inventory[item_id].quantity = quantity

    """
    Removes an item of a specified quantity from a character's inventory
    """
    def remove_item(self, item_id, quantity):
        if item_id in self.inventory:
            if self.inventory[item_id].quantity - quantity < 0:
                return -1  # Not enough items error
            elif self.inventory[item_id].quantity - quantity == 0:
                self.inventory.pop(item_id)
            else:
                self.inventory[item_id].quantity -= quantity
            return 1
        else:
            return -2  # Item not in inventory error

    """
    Displays item information for every item in a character's inventory
    """
    def display_inventory(self):
        if not self.inventory:
            return False

        print('\n{:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format("Name", "Type", "Value", "Description", "Quantity"))
        for item_id, item in self.inventory.items():
            print('{:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format(item.name, item.type, str(item.base_value) + " GP",
                                                                   item.description, str(item.quantity)))
        return True

    """
    Resets a character's inventory to be empty
    """
    def clear_inventory(self):
        self.inventory = {}


if __name__ == "__main__":
    """ CHARACTER CREATION"""
    character1 = Character("Sam", "Elf", "Warrior")
    assert character1.name == "Sam"
    assert character1.race == "Elf"
    assert character1.combat_class == "Warrior"
    assert not character1.inventory

    """ INVENTORY MANAGEMENT """
    # Add item to inventory
    character1.add_item("1", 1)
    assert character1.inventory["1"].quantity == 1
    # Remove item from inventory
    character1.remove_item("1", 1)
    assert "1" not in character1.inventory
    # Add multiple items to inventory
    character1.add_item("1", 5)
    assert character1.inventory["1"].quantity == 5
    # Remove multiple items from inventory
    character1.remove_item("1", 5)
    assert "1" not in character1.inventory
    # Remove more items than exist in inventory
    character1.add_item("1", 2)
    assert character1.inventory["1"].quantity == 2
    character1.remove_item("1", 3)
    assert character1.inventory["1"].quantity == 2
    # Clear inventory
    character1.clear_inventory()
    assert not character1.inventory
    # Try to display an empty inventory
    assert not character1.display_inventory()
    # Add item and display inventory
    character1.add_item("1", 1)
    assert character1.inventory["1"].quantity == 1
    assert character1.display_inventory()
    # Add different item and display inventory with multiple items
    character1.add_item("2", 1)
    assert character1.inventory["2"].quantity == 1
    assert character1.display_inventory()
