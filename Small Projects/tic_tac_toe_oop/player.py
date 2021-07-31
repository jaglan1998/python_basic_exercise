import random
import math


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        while not valid_move:
            try:
                position = int(input("Enter the position 1-9: "))
                if position not in game.available_moves:
                    raise ValueError
                valid_move = True
            except ValueError:
                print("Value Error. Try again.")
        return position


class RandomBotPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        position =  random.choice(game.available_moves)
        return position



