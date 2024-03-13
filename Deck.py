from Card import Creature, Resource
from random import shuffle


class Deck:
    cards = []

    def shuffle_deck(self):
        shuffle(self.cards)

    def __init__(self):
        # Create a deck of 5 cards:
        # 3 creature 2 resource
        creature1 = Creature("Creature 1")
        creature2 = Creature("Creature 2")
        creature3 = Creature("Creature 3")
        #creature1 = Creature("Creature 4", attack=2 defense=1)
        resource1 = Resource("Resource 1")
        resource2 = Resource("Resource 2")

        # add cards to deck
        self.cards.append(creature1)
        self.cards.append(creature2)
        self.cards.append(creature3)
        self.cards.append(resource1)
        self.cards.append(resource2)

        # shuffle the deck
        self.shuffle_deck()


new_deck = Deck()

for card in new_deck.cards:
    print(card)
