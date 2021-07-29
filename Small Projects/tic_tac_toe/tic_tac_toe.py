# board is the list of 9 items where we can store the position of X or 0
# outside the function all variables are global
import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

winner = None  # no one is winner yet
game_is_going = True  # true as the game is on and no winner or tie yet

computer_player = 'X'
human_player = '0'
print(f"Computer player is {computer_player} and human player is {human_player}.\n")
print("The first turn is random computer or human.\n")
current_player = random.choice([computer_player, human_player])

# current_player = input("\nChoose X or 0: ").upper()  # lets say the player is X
# while current_player not in ['X', '0']:
#     current_player = input("\nInvalid character. Choose X or 0: ").upper()


# displays the items stored in board list with help of indexing
def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def empty_board():
    if 'X' or "0" in board:
        return True





# to get the next valid move/position, displays that move on the board
def next_move():
    global current_player, board

    while True:  # ask position, if not valid nest loop that part, if empty space draw value, if not loops back here
        if current_player == computer_player:
            position = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
            index = int(position) - 1
            if board[index] == '-':  # if the selected position is empty '-' only then we can
                board[index] = current_player  # add current player e.g. 'X' on that
                break
            elif board[index] == 'X' or board[index] == '0':  # otherwise shows the try again message
                continue  # keep continue the loop until we get valid input and valid '-' blank space
        else:
            position = input("Choose a position from 1-9: ")  # we -1 to make it index as index start from 0
            while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:  # checks if input is valid or
                position = input("Invalid character. Choose a position from 1-9: ")  # otherwise loops back
            index = int(position) - 1
            if board[index] == '-':  # if the selected position is empty '-' only then we can
                board[index] = current_player  # add current player e.g. 'X' on that
                break  # every thing is fine, will add value on board
            elif board[index] == 'X' or board[index] == '0':  # otherwise shows the try again message
                print("\nAlready used spot, try again.....")
                continue  # keep continue the loop until we get valid input and valid '-' blank space



    board[index] = current_player
    return display_board()


# checks rows for winner
def check_rows():
    global winner
    if board[0] == board[1] == board[2] != '-':  # if all the spots are equal but not empty
        winner = board[0]  # winner will be the value of any of those spots
    elif board[3] == board[4] == board[5] != '-':
        winner = board[3]
    elif board[6] == board[7] == board[8] != '-':
        winner = board[6]
    return winner


# checks columns for winner
def check_columns():
    global winner
    if board[0] == board[3] == board[6] != '-':  # if all the spots are equal but not empty
        winner = board[0]  # winner will be the value of any of those spots
    elif board[1] == board[4] == board[7] != '-':
        winner = board[1]
    elif board[2] == board[5] == board[8] != '-':
        winner = board[2]
    return winner


# checks diagonals for winner
def check_diagonals():
    global winner
    if board[0] == board[4] == board[8] != '-':  # if all the spots are equal but not empty
        winner = board[0]  # winner will be the value of any of those spots
    elif board[6] == board[4] == board[2] != '-':
        winner = board[6]
    return winner


# check the winner if any, then false the game_is_going
def check_for_winner():
    global game_is_going
    check_rows()
    check_columns()
    check_diagonals()
    if winner == 'X' or winner == '0':
        game_is_going = False
    elif winner is None and '-' not in board:  # if no winner and no space left
        game_is_going = False  # its a tie and game stops
    return


# it flips the player one after other
def flip_the_players():
    global current_player
    if current_player == "X":
        current_player = '0'
    elif current_player == '0':
        current_player = 'X'
    return current_player


# function to execute the other functions step wise to play the game
def play_game():
    global current_player  # using global variable concept
    global game_is_going

    if current_player == human_player and empty_board():
        display_board()  # step 1 - we just see the blank display board with '-'

    while game_is_going:  # will keep looping while the game is going, which is true
        if current_player == human_player:
            print(f"\n...........Its' your turn.........\n")  # step 2 - tells the turn
        else:
            print("\n")
        next_move()  # step 3 - input valid move, displays it
        check_for_winner()  # step 4 - check the winner if any, then false the game_is_going
        flip_the_players()  # step 5 - if no winner flip the players to loop back again

    # here the game ends
    if winner == 'X' or winner == '0':
        print(f"\n{winner} won the game......")
    elif winner is None:
        print("\nIts a tie")


play_game()
input("\nPress any key to exit......")