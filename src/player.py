"""

"""
from item import *


class Player:
    def __init__(self, name, race, region):
        self.name = name
        self.race = race
        self.region = region
        self.inventory = {}

    def add_item(self, item_id, quantity):
        if item_id in self.inventory:
            self.inventory[item_id].quantity += 1
        else:
            self.inventory[item_id] = Item(item_id)
            self.inventory[item_id].quantity = quantity
        print("\n" + str(quantity), self.inventory[item_id].name + "(s) added to your inventory.")

    def remove_item(self, item_id, quantity):
        if item_id in self.inventory:
            if self.inventory[item_id].quantity - quantity < 0:
                print("\nInventory error. Not enough " + self.inventory[item_id].name + "s.")
                return
            elif self.inventory[item_id].quantity - quantity == 0:
                self.inventory.pop(item_id)
            else:
                self.inventory[item_id].quantity -= quantity
            print("\n" + str(quantity), Item(item_id).name + "(s) removed from your inventory.")
        else:
            print("\nInventory error. Item doesn't exist.")

    def display_inventory(self):
        if not self.inventory:
            print("\nInventory is empty.")
            return

        print('\n{:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format("Name", "Type", "Value", "Description", "Quantity"))
        for item_id, item in self.inventory.items():
            print('{:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format(item.name, item.type, str(item.base_value) + " GP",
                                                                   item.description, str(item.quantity)))

    def clear_inventory(self):
        self.inventory = {}


if __name__ == "__main__":
    """ PLAYER CREATION"""
    player1 = Player("Sam", "elf", "north")
    print(player1.name + " is an " + player1.race + " from the " + player1.region + " region.")

    """ INVENTORY MANAGEMENT """
    # Add item to inventory
    player1.add_item("1", 1)
    # Remove item from inventory
    player1.remove_item("1", 1)
    # Add multiple items to inventory
    player1.add_item("1", 5)
    # Remove multiple items from inventory
    player1.remove_item("1", 5)
    # Remove more items than exist in inventory
    player1.add_item("1", 2)
    player1.remove_item("1", 3)
    # Clear inventory
    player1.clear_inventory()
    # Display empty inventory
    player1.display_inventory()
    # Add item and display inventory
    player1.add_item("1", 1)
    player1.display_inventory()
    # Add different item and display inventory with multiple items
    player1.add_item("2", 1)
    player1.display_inventory()
