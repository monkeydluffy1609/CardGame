"""
Each player starts the game with 10 life points.
 The game ends when one player has 0 or less life points.

 Each player gets a deck of 20 cards.
 Each deck consists of the following cards:
 > 8 resources
 > 8 creatures
 > 2 spells (1 of each)
 > 2 equipment ( 1 of each)
"""


class Player:
    life_points = 10
    name = None  # or ""

    def is_player_alive(self):
        # returns True if alive or False if dead.
        # dead means their life points are 0 or less
        if self.life_points <= 0:
            return False
        else:
            return True

    def set_name(self, new_name):
        self.name = new_name

    def lose_life(self):
        pass

    def gain_life(self):
        pass


