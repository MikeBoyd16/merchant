"""
The Location class
"""
import json
with open('data/location_data.json') as data_file:
    shop_data = json.load(data_file)


class Location:
    def __init__(self, location_id):
        self.id = location_id
        self.name = shop_data[self.id]["name"]
        self.parent_location = shop_data[self.id]["parent_location"]
        self.sub_locations = shop_data[self.id]["sub_locations"]
        self.connections = shop_data[self.id]["connections"]
        self.property_value = shop_data[self.id]["property_value"]


if __name__ == "__main__":
    location1 = Location("1")
    assert location1.id == "1"
    assert location1.name == shop_data[location1.id]["name"]
    assert location1.parent_location == shop_data[location1.id]["parent_location"]
    assert location1.sub_locations == shop_data[location1.id]["sub_locations"]
    assert location1.connections == shop_data[location1.id]["connections"]
    assert location1.property_value == shop_data[location1.id]["property_value"]
