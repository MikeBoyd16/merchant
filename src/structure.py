"""
The Structure class
"""
import json
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
        self.interiors = self.load_interiors(structure_data[self.id]["interior_references"])

    def load_interiors(self, references):
        return references


if __name__ == "__main__":
    structure1 = Structure("1")
    assert structure1.id == "1"
    assert structure1.name == structure_data[structure1.id]["name"]
