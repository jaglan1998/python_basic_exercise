import random
import time

board = {k: ' ' for k in range(1, 10)}  # dict compression
winner = None  # no one is winner yet
game_is_going = True  # true as the game is on and no winner or tie yet

def select_player(letter):  # slect the player accoding to letter 'X' or 'O'.
    print("Player options Genius Bot (G), Human (H), Random Bot (R).")    
    # player = None
    while True:  # gets valid input, break if valid, continue if not 
        user_input = input(f"Enter {letter} player: ").upper()
        if user_input == 'R':
            player = 'random_bot'
            break
        elif user_input == 'H':
            player = 'human'
            break
        elif user_input == 'G':
            player = 'genius_bot'
            break
        else:
            print('Try again.')
            continue
    return player
    

def display_board():  # displays the board items
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(' ') # empty line


# need to understand and comment this section
def minimax(board, depth, isMaximizing): # minimax alogrithem
    if check_for_win(genius): # score if x_player (samrt) player wins
        return 1
    elif check_for_win(other): # score -1 other player wins
        return -1
    elif check_draw():  # score 0 if draw
        return 0

    if isMaximizing:  # when we are maximizing,
        best_score = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = genius[1]
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = other[1]
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score


def make_move(player):  # makes move according to the player
    global board  # as we changing the board variable, so need to call it globally
    available_moves = [k for k, v in board.items() if v == ' ']  # list of available moves
    move = 0  # making a move variable
    if player[0] == 'random_bot':  # move for random bot
        move = random.choice(available_moves)  # random move

    elif player[0] == 'genius_bot':  # move for genius move
        best_score = -800
        move = 0
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player[1]
                score = minimax(board, 0, False)
                board[key] = ' '
                if score > best_score:
                    best_score = score
                    move = key

    elif player[0] == 'human':  # move for human player
        try:
            move = int(input("Enter you move from 1-9: "))
            while move not in available_moves:  # looping untill get the available moves
                move = int(input("Try again. Enter you move from 1-9: "))
        except ValueError:  # except the value error if not integer
            print("Try again. Value Error")

    board[move] = player[1]  # making move, move is index, player[1] is letter of the player
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
    return False


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

    while game_is_going and not check_draw():  # will keep looping while the game is going, which is true
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


x_player = [select_player('X'), 'X']
o_player = [select_player('0'), '0']
genius = None
other = None
if o_player[0] == 'genius_bot':
    genius = o_player
    other = x_player
else:
    genius = x_player
    other = o_player

play_game()
input("\nPress any key to exit......")
