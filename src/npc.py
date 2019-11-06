"""
The Player class
"""
from character import *


class NPC(Character):
    def __init__(self, name, race, combat_class):
        super().__init__(name, race, combat_class)


if __name__ == "__main__":
    """ NPC CREATION"""
    npc1 = NPC("Sam", "Elf", "Warrior")
    assert npc1.name == "Sam"
    assert npc1.race == "Elf"
    assert npc1.combat_class == "Warrior"
    assert not npc1.inventory

    """ INVENTORY MANAGEMENT """
    # Add item to inventory
    npc1.add_item("1", 1)
    assert npc1.inventory["1"].quantity == 1
    # Remove item from inventory
    npc1.remove_item("1", 1)
    assert "1" not in npc1.inventory
    # Add multiple items to inventory
    npc1.add_item("1", 5)
    assert npc1.inventory["1"].quantity == 5
    # Remove multiple items from inventory
    npc1.remove_item("1", 5)
    assert "1" not in npc1.inventory
    # Remove more items than exist in inventory
    npc1.add_item("1", 2)
    assert npc1.inventory["1"].quantity == 2
    npc1.remove_item("1", 3)
    assert npc1.inventory["1"].quantity == 2
    # Clear inventory
    npc1.clear_inventory()
    assert not npc1.inventory
    # Display empty inventory
    npc1.display_inventory()
    # Add item and display inventory
    npc1.add_item("1", 1)
    assert npc1.inventory["1"].quantity == 1
    npc1.display_inventory()
    # Add different item and display inventory with multiple items
    npc1.add_item("2", 1)
    assert npc1.inventory["2"].quantity == 1
    npc1.display_inventory()
