import random
import math


class Player:
    def __init__(self, letter):
        self.letter = letter


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        position = None
        while True:
            position = input(f"{self.letter}'s turn. Enter the position 1-9: ")
            try:
                position = int(position)
                if position in game.available_moves():
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Value Error. Try again.")
                continue
        return position


class RandomBotPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    @staticmethod
    def get_move(game):
        position = random.choice(game.available_moves())
        return position
