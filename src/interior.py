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
        self.activity = self.load_activity(interior_data[self.id]["activity_reference"])
        self.objects = interior_data[self.id]["object_references"]
        self.connections = interior_data[self.id]["connections"]

    def load_activity(self, reference):
        return reference

    def load_objects(self, references):
        return references


if __name__ == "__main__":
    interior1 = Interior("HOUSE_MAIN_001")
    assert interior1.id == "HOUSE_MAIN_001"
    assert interior1.name == interior_data[interior1.id]["name"]
    assert interior1.connections == interior_data[interior1.id]["connections"]
