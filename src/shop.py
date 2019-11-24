"""
The Shop class
"""
import json
from activity import *
from inventory import *
with open('data/activity_data.json') as data_file:
    activity_data = json.load(data_file)


class Shop(Activity):
    def __init__(self, shop_id):
        super().__init__(shop_id, activity_data["SHOPS"][shop_id]["name"],
                         activity_data["SHOPS"][shop_id]["option_references"])
        self.owner = activity_data["SHOPS"][self.id]["owner"]
        self.greeting = activity_data["SHOPS"][self.id]["greeting"]
        self.job_wages = activity_data["SHOPS"][self.id]["job_wages"]
        self.job_roster = activity_data["SHOPS"][self.id]["job_roster"]
        self.item_references = activity_data["SHOPS"][self.id]["item_references"]
        self.hours_of_operation = activity_data["SHOPS"][self.id]["hours_of_operation"]
        self.inventory = Inventory(activity_data["SHOPS"][self.id]["item_references"])

    def run(self):
        print(self.greeting())
        run_shop = True
        while run_shop:
            response = input().upper()
            if response == "BUY":
                self.buy_goods()
            elif response == "SELL":
                self.sell_goods()
            elif response == "QUIT":
                run_shop = False

    def buy_goods(self):
        keep_buying = True
        while keep_buying:
            self.inventory.display_items_numbered()

    def sell_goods(self):
        keep_selling = True
        while keep_selling:
            self.inventory.display_items_numbered()


if __name__ == "__main__":
    shop1 = Shop("SHOP_001")
