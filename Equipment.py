from Card import Card


class Equipment(Card):
    equipment_type = None  # one of two types [+1 weapon; +1 shield]
    sword = None
    shield = None

    def set_equipment_type(self, new_equipment_type):
        self.equipment_type = new_equipment_type


# Creating equipment cards
spell1 = "Block"
spell2 = "DestroyCreature"
