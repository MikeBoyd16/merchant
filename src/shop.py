"""
The Shop class
"""
from activity import *
from inventory import *
with open('data/activity_data.json') as data_file:
    activity_data = json.load(data_file)


class Shop(Activity):
    def __init__(self, shop_id):
        super().__init__(shop_id, activity_data["SHOPS"][shop_id]["name"],
                         activity_data["SHOPS"][shop_id]["option_references"])

        # Store details
        self.owner = activity_data["SHOPS"][self.id]["owner"]
        self.job_wages = activity_data["SHOPS"][self.id]["job_wages"]
        self.job_roster = activity_data["SHOPS"][self.id]["job_roster"]
        self.item_references = activity_data["SHOPS"][self.id]["item_references"]
        self.hours_of_operation = activity_data["SHOPS"][self.id]["hours_of_operation"]
        self.inventory = Inventory(activity_data["SHOPS"][self.id]["item_references"])

        # Dialogue
        self.current_dialogue = ""
        self.greeting = activity_data["SHOPS"][self.id]["greeting"]
        self.thank_you_message = activity_data["SHOPS"][self.id]["thank_you_message"]
        self.not_enough_message = activity_data["SHOPS"][self.id]["not_enough_message"]
        self.custom_options = activity_data["SHOPS"][self.id]["custom_options"]

    def run(self):
        print(self.greeting)
        self.display_options()
        while True:
            response = input()
            if response.isnumeric():
                response = int(response)
                if response == 1:
                    self.buy_goods()
                elif response == 2:
                    self.sell_goods()
                elif response == 5:
                    return

            print("\nAre there any other services I can provide?")
            self.display_options()

    def buy_goods(self):
        clerk_dialogue = "Which item?"
        keep_buying = True
        while keep_buying:
            print("\n" + self.name)
            self.inventory.display_items_numbered()
            print("\n" + clerk_dialogue)
            waiting = True
            while waiting:
                # Get the number of the item
                response = input()
                if response.upper() == "QUIT":
                    return
                elif response.isnumeric():
                    item_num = int(response)
                    if 1 <= item_num <= len(self.inventory.inventory_items):
                        # Get the item ID
                        item_id = self.inventory.inventory_items[item_num - 1].id

                        # Get the quantity to purchase
                        response = input("How many?\n")
                        if response.upper() == "QUIT":
                            waiting = False
                        elif response.isnumeric():
                            quantity = int(response)
                            if self.inventory.remove_item(item_id, quantity) == -1:
                                clerk_dialogue = self.not_enough_message
                            else:
                                clerk_dialogue = self.thank_you_message

                            waiting = False

    def sell_goods(self):
        keep_selling = True
        while keep_selling:
            self.inventory.display_items_numbered()

    def display_options(self):
        print("\n1. I would like to purchase some goods." +
              "\n2. I would like to sell some goods.", end=" ")
        for option in self.custom_options:
            print(option, end=" ")
        print("\n" + str(len(self.custom_options) + 3) + ". (leave)\n")


if __name__ == "__main__":
    shop1 = Shop("SHOP_001")
    shop1.run()
