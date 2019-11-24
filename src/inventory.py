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
        for item in self.inventory_items:
            if item_id == item.id:
                item.quantity += quantity
                return

        new_item = Item(item_id)
        new_item.quantity = quantity
        self.inventory_items.append(new_item)

    """
    Removes an item of a specified quantity
    """
    def remove_item(self, item_id, quantity):
        for item in self.inventory_items:
            if item_id == item.id:
                if item.quantity - quantity < 0:
                    return -1  # Not enough items error
                elif item.quantity - quantity == 0:
                    self.inventory_items.remove(item)
                else:
                    item.quantity -= quantity
                return 1
            else:
                return -2  # Item not in inventory error

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
        if not self.inventory_items:
            return False

        print('\n{:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format("Name", "Type", "Value", "Description", "Quantity"))
        for item in self.inventory_items:
            print('{:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format(item.name, item.type, str(item.base_value) + " GP",
                                                                   item.description, str(item.quantity)))
        return True

    """
    Displays item information for every item in a numbered format
    """
    def display_items_numbered(self):
        if not self.inventory_items:
            return False

        print('\n{:<5s} {:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format("#", "Name", "Type", "Value", "Description",
                                                                        "Quantity"))

        item_num = 1
        for item in self.inventory_items:
            print('{:<5s} {:<20s} {:<15s} {:<10s} {:<20s} {:<15s}'.format(str(item_num), item.name, item.type,
                                                                          str(item.base_value) + " GP",
                                                                          item.description, str(item.quantity)))
            item_num += 1

        return True


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
