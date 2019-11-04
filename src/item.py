"""

"""


class Item:
    def __init__(self, name, item_type, value, description):
        self.name = name
        self.item_type = item_type
        self.value = value
        self.description = description


if __name__ == "__main__":
    item1 = Item("Health Potion", "Consumable", 15, "Restores 25 HP")
    print(item1.name + " is a " + item1.item_type + " that costs " +
          str(item1.value) + " gold and " + item1.description)
