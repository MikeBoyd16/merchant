"""
Main
"""
from character import *
from location import *
from npc import *
from player import *

import json
from structure import *
with open('data/location_data.json') as data_file:
    location_data = json.load(data_file)


if __name__ == "__main__":
    world = []
    for reference in location_data:
        world.append(Location(reference))

    for location in world:
        print(location.name)
        for structure in location.structures:
            print("\t" + structure.name)
            for interior in structure.interiors:
                print("\t\t" + interior.name)
