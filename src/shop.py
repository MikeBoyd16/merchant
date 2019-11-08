"""
The Shop class
"""
from location import *
with open('data/shop_data.json') as data_file:
    shop_data = json.load(data_file)


class Shop(Location):
    def __init__(self, location_id, shop_id):
        super().__init__(location_id)
        self.id = shop_id
        self.name = shop_data[self.id]["name"]
        self.owner = shop_data[self.id]["owner"]
        self.jobs = shop_data[self.id]["jobs"]
        self.inventory = shop_data[self.id]["inventory"]
        self.hours_of_operation = shop_data[self.id]["hours_of_operation"]
        self.current_npcs = shop_data[self.id]["current_npcs"]


if __name__ == "__main__":
    """ SHOP CREATION """
    shop1 = Shop("2", "1")
    assert shop1.id == "1"
    assert shop1.name == shop_data[shop1.id]["name"]
    assert shop1.owner == shop_data[shop1.id]["owner"]
    assert shop1.jobs == shop_data[shop1.id]["jobs"]
    assert shop1.inventory == shop_data[shop1.id]["inventory"]
    assert shop1.hours_of_operation == shop_data[shop1.id]["hours_of_operation"]
    assert shop1.current_npcs == shop_data[shop1.id]["npcs"]
