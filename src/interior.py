"""
The Interior class
"""
import json
from shop import *
with open('data/interior_data.json') as data_file:
    interior_data = json.load(data_file)


class Interior:
    def __init__(self, location_id):
        self.id = location_id
        self.name = interior_data[self.id]["name"]
        self.activities = []
        self.init_activity(interior_data[self.id]["activity_references"])
        self.objects = interior_data[self.id]["object_references"]
        self.connections = interior_data[self.id]["connections"]

    def init_activity(self, references):
        for reference in references:
            if reference[:4] == "SHOP":
                self.activities.append(Shop(reference))

    def init_objects(self, references):
        return references


if __name__ == "__main__":
    interior1 = Interior("GG_MAIN_HALL_001")
    assert interior1.id == "GG_MAIN_HALL_001"
    assert interior1.name == interior_data[interior1.id]["name"]
    assert interior1.connections == interior_data[interior1.id]["connections"]
