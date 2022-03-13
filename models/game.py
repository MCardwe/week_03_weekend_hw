
class Game:
    def __init__(self, player_1, player_2):
        self.player_1_choice = player_1
        self.player_2_choice = player_2

    
    def get_winner(self):
        game_rules = {
            "rock":"paper",
            "paper":"scissors",
            "scissors":"rock"
        }

        player_1 = game_rules[self.player_1_choice]
        if player_1 == self.player_2_choice:
            return "player 2 wins"
        elif self.player_1_choice == self.player_2_choice:
            return "Its a draw"
        else:
            return "player 1 wins"