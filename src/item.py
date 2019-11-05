"""

"""


class Item:
    def __init__(self, item_id, name, item_type, base_value, description):
        self.id = item_id
        self.name = name
        self.type = item_type
        self.base_value = base_value
        self.description = description
        self.quantity = 0


if __name__ == "__main__":
    item1 = Item(1, "Health Potion", "Consumable", 15, "Restores 25 HP")
    print(item1.name + " is a " + item1.type + " that costs " +
          str(item1.base_value) + " gold and " + item1.description)
