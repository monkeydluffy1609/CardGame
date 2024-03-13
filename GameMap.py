"""
Trees
Buildings
Windows
Mini Map
Treasure Map
Full Map [Display entire view of land]
Scoreboard
"""


class Map:
    minimap = True
    building = True
    trees = True
    windows = True
    scoreboard = True

    def is_window(self):
        if self.windows:
            return True