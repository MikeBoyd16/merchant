"""
The Structure class
"""
import json
from interior import *
with open('data/structure_data.json') as data_file:
    structure_data = json.load(data_file)


class Structure:
    def __init__(self, location_id):
        self.id = location_id
        self.name = structure_data[self.id]["name"]
        self.type = structure_data[self.id]["type"]
        self.owner = structure_data[self.id]["owner"]
        self.is_sellable = structure_data[self.id]["is_sellable"]
        self.is_listed = structure_data[self.id]["is_listed"]
        self.property_value = structure_data[self.id]["property_value"]
        self.interiors = []
        self.init_interiors(structure_data[self.id]["interior_references"])

    def init_interiors(self, references):
        for reference in references:
            self.interiors.append(Interior(reference))


if __name__ == "__main__":
    structure1 = Structure("HOUSE_001")
    assert structure1.id == "HOUSE_001"
    assert structure1.name == structure_data[structure1.id]["name"]
