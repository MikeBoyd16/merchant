"""
The Interior class
"""
import json
with open('data/interior_data.json') as data_file:
    interior_data = json.load(data_file)


class Interior:
    def __init__(self, location_id):
        self.id = location_id
        self.name = interior_data[self.id]["name"]
        self.activity_references = interior_data[self.id]["activity_references"]
        self.object_references = interior_data[self.id]["object_references"]
        self.connections = interior_data[self.id]["connections"]


if __name__ == "__main__":
    interior1 = Interior("GG_MAIN_HALL_001")
    assert interior1.id == "GG_MAIN_HALL_001"
    assert interior1.name == interior_data[interior1.id]["name"]
    assert interior1.connections == interior_data[interior1.id]["connections"]
