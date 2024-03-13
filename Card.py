class Card:
    card_type = None


class Creature(Card):
    attack_strength = 1
    defense_strength = 1
    resource_cost = 1

    def __init__(self, creature_name):
        self.card_type = "Creature"
        self.name = creature_name

    def __str__(self):
        message = self.name + \
         " Attack: " + str(self.attack_strength) +\
         " Defense:" + str(self.defense_strength) +\
         " Cost: " + str(self.resource_cost)
        return message

class Resource(Card):
    def __init__(self, resource_name):
        self.card_type = "Resource"
        self.resource = resource_name

