import game
import player


class TicTacToe:
    def __init__(self):
        # self.board = {}
        # for k in range(1, 10):
        #     self.board[k] = " "
        self.board = {k: " " for k in range(1, 10)}  # dict comprehension
        self.current_winner = None

    def print_board(self):
        print(self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print(self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[5])
        print(self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])

    def available_moves(self):
        # moves = []
        # for k, v in self.board.items():
        #     if v == ' ':
        #         moves.append(k)
        # return moves
        return [k for k, v in self.board.items() if v == ' ']


def play(game, x_player, o_player, print_game=True):
    game = TicTacToe()
    x_player = player.RandomBotPlayer('X')
    o_player = player.HumanPlayer('O')



g = TicTacToe()
print(g.available_moves())








