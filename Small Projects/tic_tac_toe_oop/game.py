from player import Player, HumanPlayer, RandomBotPlayer


class TicTacToe:
    def __init__(self):
        # self.board = {}
        # for k in range(1, 10):
        #     self.board[k] = " "
        self.board = {k: " " for k in range(1, 10)}  # dict comprehension
        self.current_winner = None
        self.game_is_on = True

    def print_board(self):  # need to find the NONE bug
        print(self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print(self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print(self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])

    def available_moves(self):
        # moves = []
        # for k, v in self.board.items():
        #     if v == ' ':
        #         moves.append(k)
        # return moves
        return [k for k, v in self.board.items() if v == ' ']

    def empty_position(self):
        if ' ' in self.board.values():
            return True

    def check_for_winner(self, letter):
        if self.board[1] == self.board[2] == self.board[3] == letter:
            return True
        elif self.board[4] == self.board[5] == self.board[6] == letter:
            return True
        elif self.board[7] == self.board[8] == self.board[9] == letter:
            return True
        elif self.board[1] == self.board[4] == self.board[7] == letter:
            return True
        elif self.board[2] == self.board[5] == self.board[8] == letter:
            return True
        elif self.board[3] == self.board[6] == self.board[9] == letter:
            return True
        elif self.board[1] == self.board[5] == self.board[9] == letter:
            return True
        elif self.board[3] == self.board[5] == self.board[7] == letter:
            return True
        return

    def make_move(self, position, letter):
        if self.board[position] == ' ':
            self.board[position] = letter


def play(game, x_player, o_player):
    game.print_board()
    letter = 'X'

    while game.game_is_on and game.empty_position():
        if letter == 'O':
            position = o_player.get_move(game)
        else:
            position = x_player.get_move(game)

        game.make_move(position, letter)
        print(f"{letter} makes a move to position {position}")
        game.print_board()
        print(" ")
        if game.check_for_winner(letter):
            print(f"{letter} wins.")
            game.game_is_on = False
            game.current_winner = letter
            break
        letter = 'O' if letter == 'X' else 'X'
    if game.current_winner not in ['X', 'O']:
        print("Its a tie")


if __name__ == '__main__':
    t = TicTacToe()
    x_player = RandomBotPlayer('X')
    o_player = RandomBotPlayer('O')

    play(t, x_player, o_player)
