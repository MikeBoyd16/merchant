"""
The Location class
"""
import json
with open('data/location_data.json') as data_file:
    location_data = json.load(data_file)


class Location:
    def __init__(self, location_id):
        self.id = location_id
        self.name = location_data[self.id]["name"]
        self.parent_location = location_data[self.id]["parent_location"]
        self.sub_locations = location_data[self.id]["sub_locations"]
        self.connections = location_data[self.id]["connections"]
        self.npcs = location_data[self.id]["npcs"]


if __name__ == "__main__":
    location1 = Location("1")
    assert location1.id == "1"
    assert location1.name == "Garden Grove Market"
    assert location1.parent_location == "Eastbrook"
    assert location1.sub_locations == [2]
    assert location1.connections == {"3": 10, "4": 2, "5": 2}
    assert location1.npcs == [2, 3]
