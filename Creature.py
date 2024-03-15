from Card import Card


# Child class of Card class
class Creature(Card):
    attack_strength = 1
    defense_strength = 1
    resource_cost_to_cast_card = 1
    creature_type = None # e.g., warrior, wizard, elf, dragon, witch, etc.

    # Constructor
    def __init__(self, creature_name, attack_strength, defense_strength, resource):
        self.creature_name = creature_name
        self.card_type = "Creature"
        self.attack_strength = attack_strength
        self.defense_strength = defense_strength
        self.resource_cost_to_cast_card = resource

    def __str__(self):
        message = self.creature_name + \
            " - Attack:" + str(self.attack_strength) + \
            " Defense:" + str(self.defense_strength) + \
            " Cost:" + str(self.resource_cost_to_cast_card)
        return message


# Create a bunch of creature cards

# 1 resource creatures
creature1 = Creature(attack_strength=1, defense_strength=1, resource=1)

# 2 resource creatures
creature2 = Creature(attack_strength=1, defense_strength=2, resource=2)
creature3 = Creature(attack_strength=2, defense_strength=1, resource=2)

# 3 resource creatures
creature4 = Creature(attack_strength=3, defense_strength = 1, resource=3)
creature5 = Creature(attack_strength=1, defense_strength = 3, resource=3)

# 4 resource creatures
creature7 = Creature(attack_strength=4, defense_strength = 1, resource=4)
creature8 = Creature(attack_strength=1, defense_strength = 4, resource=4)



