import random
import sys

def start():
    # this game will be played in two versions
    print("Enter 1: You will guess the number, computer will give the feedback")
    print("Enter 2: Computer will guess the number, you will give the feedback")
    global x
    try:
        x = int(input("\nEnter you choice: "))
    except ValueError:
        print("Value Error, Try again")
        sys.exit()



def user_inputs():
    global a, b
    try:
        a = int(input("\nPlease enter the start range: "))
        b = int(input("\nPlease enter the end range: "))
    except ValueError:
        print("Value Error, Try again")
        sys.exit()



def guess(a, b):
    print("\n.......Guess a number if you find the secret no. you will win.......")
    secret_no = random.randint(a, b)
    guessed_no = None
    count = 0
    while secret_no != guessed_no:
        try:
            guessed_no = int(input(f"\nEnter you guess between the range {a} & {b}: "))
            count += 1
        except ValueError:
            print("Value Error, try again")
            count -= 1
            continue
        if a <= guessed_no <= b and guessed_no > secret_no:
            print(f"{guessed_no} is too high, try again")
        elif a <= guessed_no <= b and guessed_no < secret_no:
            print(f"{guessed_no} is too low, try again")
        elif not a <= guessed_no <= b:
            print("Please, enter only in given range. Thanks")
            count -= 1
    print(f"\nCongrats, you guessed the right number {guessed_no} in {count} try/tries.")


def computer_guess(a, b):
    print("\n.........choose a no. in mind, give feedback accordingly............")
    low = a
    high = b
    feedback = ""
    count = 0
    while feedback != 'c':
        guess = random.randint(low, high)
        count += 1
        try:
            feedback = input(f"Is guess no. is {guess}. Please, enter high(h), low(l) or correct(c): ").lower()
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
            elif feedback != 'h' and feedback != 'l' and feedback != 'c':
                print("Please, enter the valid input only.")
                count -= 1
                continue
        except ValueError:
            print("Try again, Value Error")
            count -= 1
            continue
    print(f"Computer guessed the right number {guess} in {count} try/tries.")

for i in range(3):
    start()
    if x == 1:
        user_inputs()
        guess(a, b)
        break
    elif x == 2:
        user_inputs()
        computer_guess(a, b)
        break
    else:
        print("Please enter the valid input")
        continue













