"""
The Inventory class
"""
from item import *


class Inventory:
    def __init__(self, item_references=None):
        self.inventory_items = []
        if item_references:
            self.init_inventory_items(item_references)

    """
    Adds an item of a specified quantity
    """
    def add_item(self, item_id, quantity):
        item = self.get_item(item_id)
        if item:
            item.quantity += quantity
            return

        new_item = Item(item_id)
        new_item.quantity = quantity
        self.inventory_items.append(new_item)

    """
    Removes an item of a specified quantity
    """
    def remove_item(self, item_id, quantity):
        item = self.get_item(item_id)
        if item:
            if item.quantity - quantity < 0:
                return -1  # Not enough items error
            elif item.quantity - quantity == 0:
                self.inventory_items.remove(item)
            else:
                item.quantity -= quantity
            return 1

    """
    Get the item that corresponds with the item ID
    """
    def get_item(self, item_id):
        for item in self.inventory_items:
            if item_id == item.id:
                return item

    """
    Initializes an inventory's default items
    """
    def init_inventory_items(self, item_references):
        for item_id, quantity in item_references.items():
            new_item = Item(item_id)
            new_item.quantity = quantity
            self.inventory_items.append(new_item)

    """
    Resets an inventory to be empty
    """
    def clear_inventory(self):
        self.inventory_items = []

    """
    Displays item information for every item
    """
    def display_items(self):
        print('{:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format("Name", "Type", "Value", "Description", "Quantity"))
        if not self.inventory_items:
            print("No items")
        else:
            for item in self.inventory_items:
                print('{:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format(item.name, item.type, str(item.base_value) +
                                                                       " GP", item.description, str(item.quantity)))
        print("\n")

    """
    Displays item information for every item in a numbered format
    """
    def display_items_numbered(self):
        print('{:<5s} {:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format("#", "Name", "Type", "Value", "Description",
                                                                      "Quantity"))
        if not self.inventory_items:
            print("No items")
        else:
            item_num = 1
            for item in self.inventory_items:
                print('{:<5s} {:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format(str(item_num), item.name, item.type,
                                                                              str(item.base_value) + " GP",
                                                                              item.description, str(item.quantity)))
                item_num += 1


if __name__ == "__main__":
    """ INVENTORY CREATION"""
    inventory1 = Inventory()
    inventory1.add_item("HEALTH_POTION_001", 20)
    inventory1.add_item("MANA_POTION_001", 15)
    inventory1.display_items()
    inventory1.remove_item("HEALTH_POTION_001", 5)
    inventory1.display_items_numbered()
    inventory1.remove_item("HEALTH_POTION_001", 15)
    inventory1.display_items_numbered()
