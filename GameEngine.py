from Player import Player

"""
Game Engine: [Control the overall game and its components. This is where
 the logic and rules of the game will be.]


> Allow players to enter their name [X]
> Starting a game (setup) []
> Keeping Score [X]
> Check if the game is over [X]
"""


class GameEngine:  # in contrast to Game_Engine
    player1 = Player()  # controlled by human
    opponent = Player()  # controlled by computer
    player_score = 0
    opponent_score = 0

    def get_player_name(self):
        player_name = input("Enter your name: ")
        self.player1.set_name(player_name)
        return self.player1

    def set_score(self):
        pass

    def get_score(self):
        score = 1
        if self.player1.is_player_alive() == False and self.opponent.is_player_alive() == True:
            self.opponent.score = self.opponent.score + score
        elif self.player1.is_player_alive() == True and self.opponent.is_player_alive() == False:
            self.player1.score = self.player1.score + score

    def turn(self):
        self.draw_a_card()
        self.play_resource()
        self.play_creature()
        self.play_spell()
        self.play_equipment()
        self.attack_or_defend()
        # end_turn()

    def draw_a_card(self):
        pass

    def play_resource(self):
        pass

    def play_creature(self):
        pass

    def play_spell(self):
        pass

    def play_equipment(self):
        pass

    def attack_or_defend(self):
        pass

    def setup_game(self):
        player1 = GameEngine.get_player_name()
        opponent = GameEngine.get_player_name()

    def deal_cards(self):
        pass

    def is_game_over(self):
        # check if players life <=0 or opponents life is <=0
        if self.player1.is_player_alive() and self.opponent.is_player_alive() == False:
            return False
        else:
            return True


game = GameEngine()
game.get_player_name()
print("Your name is: {}".format(game.player1.name))
new_game = GameEngine()
new_game.setup_game()
