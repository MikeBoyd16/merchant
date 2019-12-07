"""
The Game State class
"""
from location import *
from structure import *
from interior import *
with open('data/location_data.json') as data_file:
    location_data = json.load(data_file)
with open('data/structure_data.json') as data_file:
    structure_data = json.load(data_file)
with open('data/interior_data.json') as data_file:
    interior_data = json.load(data_file)


class GameState:
    def __init__(self):
        self.locations = []
        self.structures = []
        self.interiors = []
        self.load_world()

        self.current_location = self.locations[0]
        self.current_structure = self.get_structure(self.current_location.structure_references[0])
        self.current_interior = self.get_interior(self.current_structure.interior_references[0])

    def load_world(self):
        for location_reference in location_data:
            self.locations.append(Location(location_reference))
        for structure_reference in structure_data:
            self.structures.append(Structure(structure_reference))
        for interior_reference in interior_data:
            self.interiors.append(Interior(interior_reference))

    def run(self):
        keep_playing = True
        while keep_playing:
            response = input().upper()
            if response == "QUIT":
                keep_playing = False
            elif response == "ACTIONS":
                self.display_actions()
            elif response == "TRAVEL":
                self.display_areas()

    def parse_response(self):
        keywords = ["GO TO", "Hightown Commons", "The Happy Cudgel", "Carmen's Consumables"]
        return

    def get_location(self, reference):
        for location in self.locations:
            if location.id == reference:
                return location

    def get_structure(self, reference):
        for structure in self.structures:
            if structure.id == reference:
                return structure

    def get_interior(self, reference):
        for interior in self.interiors:
            if interior.id == reference:
                return interior

    def display_world(self):
        for location in self.locations:
            print(location.name)
            for structure_reference in location.structure_references:
                structure = self.get_structure(structure_reference)
                print("\t" + structure.name)
                for interior_reference in structure.interior_references:
                    interior = self.get_interior(interior_reference)
                    print("\t\t" + interior.name)

    def display_actions(self):
        pass

    def display_areas(self):
        print("Accessible areas:")
        for connection in self.current_interior.connections:
            interior = self.get_interior(connection)
            print(interior.name)


if __name__ == "__main__":
    game_state = GameState()
    game_state.display_world()
    game_state.display_areas()
