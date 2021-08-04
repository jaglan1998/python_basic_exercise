import random
import time

board = {k: ' ' for k in range(1, 10)}  # dict compression
winner = None  # no one is winner yet
game_is_going = True  # true as the game is on and no winner or tie yet

x_player = [' ', 'X']
o_player = [' ', '0']


def select_player():
    global x_player, o_player
    print("Player options Genius Bot (G), Human (H), Random Bot (R).")
    user_input = input("Enter X player: ").upper()
    if user_input == 'R':
        x_player[0] = 'random_bot'
    elif user_input == 'H':
        x_player[0] = 'human'
    elif user_input == 'G':
        x_player[0] = 'genius_bot'
    else:
        print('Try again.')
    user_input = input("Enter 0 player: ").upper()
    if user_input == 'R':
        o_player[0] = 'random_bot'
    elif user_input == 'H':
        o_player[0] = 'human'
    elif user_input == 'G':
        o_player[0] = 'genius_bot'
    else:
        print('Try again.')


def display_board():  # displays the board items
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(' ')


def minimax(board, depth, isMaximizing):
    if check_for_win(x_player):
        return 1
    elif check_for_win(o_player):
        return -1
    elif check_draw():
        return 0

    if isMaximizing:
        best_score = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = x_player[1]
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = o_player[1]
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score


def make_move(player):  # makes move according to the player
    global board
    available_moves = [k for k, v in board.items() if v == ' ']
    move = 0
    if player[0] == 'random_bot':
        move = random.choice(available_moves)
    elif player[0] == 'genius_bot':
        best_score = -800
        move = 0
        for key in board.keys():
            if board[key] == ' ':
                board[key] = x_player[1]
                score = minimax(board, 0, False)
                board[key] = ' '
                if score > best_score:
                    best_score = score
                    move = key

    elif player[0] == 'human':
        try:
            move = int(input("Enter you move from 1-9: "))
            while move not in available_moves:
                move = int(input("Try again. Enter you move from 1-9: "))
        except ValueError:
            print("Try again. Value Error")
    board[move] = player[1]
    return


def check_for_win(player):
    global winner
    if board[1] == board[2] == board[3] == player[1]:
        winner = player
        return True
    elif board[4] == board[5] == board[6] == player[1]:
        winner = player
        return True
    elif board[7] == board[8] == board[9] == player[1]:
        winner = player
        return True
    elif board[1] == board[4] == board[7] == player[1]:
        winner = player
        return True
    elif board[2] == board[5] == board[8] == player[1]:
        winner = player
        return True
    elif board[3] == board[6] == board[9] == player[1]:
        winner = player
        return True
    elif board[1] == board[5] == board[9] == player[1]:
        winner = player
        return True
    elif board[3] == board[5] == board[7] == player[1]:
        winner = player
        return True

# checks rows for winner
def check_rows():
    global winner
    if board[1] == board[2] == board[3] != '-':  # if all the spots are equal but not empty
        winner = board[1]  # winner will be the value of any of those spots
    elif board[4] == board[5] == board[6] != '-':
        winner = board[4]
    elif board[7] == board[8] == board[9] != '-':
        winner = board[7]
    return winner


def check_draw():
    if ' ' not in board.values():
        return True
    return False


# it flips the player one after other
def flip_the_players(player):
    if player[1] == "X":
        player = o_player
    elif player[1] == '0':
        player = x_player
    return player


# function to execute the other functions step wise to play the game
def play_game():
    global game_is_going, winner
    display_board()
    player = x_player  # starting player

    while game_is_going and ' ' in board.values():  # will keep looping while the game is going, which is true
        print(f"This is {player}' turn.")
        make_move(player)
        time.sleep(0.01)
        display_board()
        if check_for_win(player):
            game_is_going = False
            print(f'{winner} won the game.')
        player = flip_the_players(player)
    if check_draw():
        print('Its a tie.')


select_player()
play_game()
input("\nPress any key to exit......")