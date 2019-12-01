"""
The Location class
"""
import json
from structure import *
with open('data/location_data.json') as data_file:
    location_data = json.load(data_file)


class Location:
    def __init__(self, location_id):
        self.id = location_id
        self.name = location_data[self.id]["name"]
        self.type = location_data[self.id]["type"]
        self.region = location_data[self.id]["region"]
        self.structures = []
        self.init_structures(location_data[self.id]["structure_references"])

    def init_structures(self, references):
        for reference in references:
            self.structures.append(Structure(reference))


if __name__ == "__main__":
    location1 = Location("1")
    assert location1.id == "1"
    assert location1.name == location_data[location1.id]["name"]
    assert location1.type == location_data[location1.id]["type"]
    assert location1.region == location_data[location1.id]["region"]
