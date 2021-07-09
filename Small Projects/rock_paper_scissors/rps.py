import random
import math


def play():
    computer_score = 0
    user_score = 0
    while True:
        try:
            x = int(input("How many times you want to play the game \n(Press enter for default one time): "))
            assert (x > 0)
            break
        except AssertionError and ValueError:
            print("\n.......Number must be integer and bigger than zero........try again.....\n")

    for i in range(x):
        while True:
            user = input("\nEnter, 'r' for rock, 'p' for paper, 's' for scissors. \n")
            if user not in ['r', 'p', 's']:
                print("\n..........Invalid entry...... try again........\n")
                continue
            computer = random.choice(['r', 'p', 's'])
            if user == 'r' and computer == 's' or user == 's' and computer == 'p' or user == 'p' and computer == 'r':
                print("You won")
                user_score += 1
                break
            elif user == computer:
                print("Its a tie")
                continue
            print("You Lost")
            computer_score += 1
            break
    print(f"\nIn {x} matches, you won {user_score} times while computer won {computer_score} times.")

play()

input()
