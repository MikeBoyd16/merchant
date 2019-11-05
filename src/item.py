"""

"""
import json
with open('data/item_data.json') as data_file:
    item_data = json.load(data_file)


class Item:
    def __init__(self, item_id):
        self.id = item_id
        self.name = item_data[item_id]["name"]
        self.type = item_data[item_id]["type"]
        self.base_value = item_data[item_id]["base_value"]
        self.description = item_data[item_id]["description"]
        self.quantity = 0


if __name__ == "__main__":
    item1 = Item("1")
    print(item1.name + " is a " + item1.type + " that costs " +
          str(item1.base_value) + " gold and " + item1.description)
