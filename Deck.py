from Card import Card
from Creature import Creature
from Resource import Resource
from random import shuffle


class Deck(Card):
    cards = []

    def shuffle_deck(self):
        shuffle(self.cards)

    # creates a new deck consisting of 8 res, 8 creature, 2 spell, 2 equip
    def __init__(self):
        creature1 = Creature("Creature 1")
        creature2 = Creature("Creature 2")
        creature3 = Creature("Creature 3")
        # creature1 = Creature("Creature 4", attack=2, defense=1)
        resource1 = Resource()
        resource2 = Resource()

        # add cards to deck
        self.cards.append(creature1)
        self.cards.append(creature2)
        self.cards.append(creature3)
        self.cards.append(creature1)
        self.cards.append(resource1)
        self.cards.append(resource2)

        # shuffle the deck
        self.shuffle_deck()

new_deck = Deck()

for card in new_deck.cards:
    print(card)










