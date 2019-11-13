"""
The Shop class
"""
import json
from activity import *
with open('data/activity_data.json') as data_file:
    activity_data = json.load(data_file)


class Shop(Activity):
    def __init__(self, shop_id):
        super().__init__(shop_id, activity_data["SHOPS"][shop_id]["name"],
                         activity_data["SHOPS"][shop_id]["option_references"])
        self.owner = activity_data["SHOPS"][self.id]["owner"]
        self.jobs = activity_data["SHOPS"][self.id]["jobs"]
        self.inventory = activity_data["SHOPS"][self.id]["inventory"]
        self.hours_of_operation = activity_data["SHOPS"][self.id]["hours_of_operation"]
        self.current_npcs = activity_data["SHOPS"][self.id]["current_npcs"]


if __name__ == "__main__":
    """ SHOP CREATION """
    shop1 = Shop("SHOP_001")
    assert shop1.id == "SHOP_001"
    assert shop1.name == activity_data["SHOPS"][shop1.id]["name"]
    assert shop1.owner == activity_data["SHOPS"][shop1.id]["owner"]
    assert shop1.jobs == activity_data["SHOPS"][shop1.id]["jobs"]
    assert shop1.inventory == activity_data["SHOPS"][shop1.id]["inventory"]
    assert shop1.hours_of_operation == activity_data["SHOPS"][shop1.id]["hours_of_operation"]
    assert shop1.current_npcs == activity_data["SHOPS"][shop1.id]["current_npcs"]
    assert shop1.options == activity_data["SHOPS"][shop1.id]["option_references"]
