"""
The Game State class
"""
from location import *
with open('data/location_data.json') as data_file:
    location_data = json.load(data_file)


class GameState:
    def __init__(self):
        self.world = []
        self.load_world()

        self.current_location = self.world[0]
        self.current_structure = self.current_location.structures[0]
        self.current_interior = self.current_structure.interiors[0]

    def load_world(self):
        for reference in location_data:
            self.world.append(Location(reference))

    def display_actions(self):
        pass

    def display_areas(self):
        print("Accessible areas:")
        for connection in self.current_interior.connections:
            print(self.get_interior_name(connection))

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

    def get_interior_name(self, reference):
        for location in self.world:
            for structure in location.structures:
                for interior in structure.interiors:
                    if reference == interior.id:
                        return interior.name


if __name__ == "__main__":
    game_state = GameState()
    game_state.display_areas()
