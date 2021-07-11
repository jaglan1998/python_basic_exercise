import random
from words import word_list  # import list from different file
import string


def get_valid_word(lst, a, b):  # gets a valid word (without ' ' or '-') in word range a, b
    valid_word_list = list()  # valid words get stored here
    for words in lst:
        if " " in words or '-' in words:  # do nothing if words are not valid
            pass
        elif a <= len(words) <= b:
            valid_word_list.append(words)
    hangman_word = random.choice(valid_word_list).upper()  # random word from valid_word_list in uppercase
    return hangman_word


def game_level():
    while True:  # loops around until you get the right input, except the value error
        try:
            x = int(input("Enter the game level easy (1), medium (2) or hard (3): "))
            if x == 1 or x == 2 or x == 3:
                break  # if the input is right it breaks the loop
            print("\nInvalid entry......try again......\n")
            continue  # if input is invalid, will keep looping
        except ValueError:
            print("\nInvalid entry......try again......\n")
            continue

    # game level selections

    if x == 1:
        print("\n....easy level... no. of characters 3-5\n")
        hangman_word = (get_valid_word(word_list, 3, 5))
    elif x == 2:
        print("\n....medium level... no. of characters 6-9\n")
        hangman_word = (get_valid_word(word_list, 6, 9))
    elif x == 3:
        print("\n....hard level... no. of characters 10-14\n")
        hangman_word = (get_valid_word(word_list, 10, 14))

    return hangman_word


def hangman():
    hangman_word = game_level()  # the random word which is clean/valid and according to the game level
    # print("Hangman word = ", hangman_word)
    hangman_word_letters = set(hangman_word)  # set of all letters in hangman_word
    # print("Hangman word letters = ", hangman_word_letters)

    all_alphabets = set(string.ascii_uppercase)
    # print(all_alphabets)

    used_letters = set()  # the letters which we have used for guess

    lives = 10
    random_valid_hint = list(hangman_word_letters - used_letters)

    easy_counter = 0  # it is just a bug fixing for lines 100-105

    # keeps asking input until all letters get guessed and still have lives left
    while len(hangman_word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left. ")
        print("\nYou have used these letters so far: ", ' '.join(used_letters))  # join letters in format A B C D

        # list of words which are in word but not in used yet, for hint purpose
        random_valid_hint = list(hangman_word_letters - used_letters)

        # hangman_word_list = list()
        # for letter in hangman_word:
        #     if letter in used_letters:
        #         hangman_word_list.append(letter)
        #     else:
        #         hangman_word_list.append('-')
        # short form of this code is below one

        hangman_word_list = [letter if letter in used_letters else '-' for letter in hangman_word]

        print("Hangman word problem: ", ' '.join(hangman_word_list))  # prints elements above list in A B C D form

        guess_letter = input("Enter a guess letter: ").upper()  # user input, upper case function

        if guess_letter in all_alphabets - used_letters:  # if the guess letter is in alphabet but not used yet
            used_letters.add(guess_letter)  # then we add this guess letter to used letter as it just get used
            # if the guess is right means if that letter is in hangman_word_letters
            if guess_letter in hangman_word_letters:
                # then remove that element from the list as we getting closer to solve the problem
                hangman_word_letters.remove(guess_letter)
            else:  # if its not right letter that means its its wrong
                lives -= 1  # so we will take away the live

        elif guess_letter in used_letters:  # if letter is already in used letter
            print("\n....You have already used this letter. Please try again......\n")

        elif guess_letter == 'HINT':  # special case if we type hint than do this
            print("\nYour hint is: ", random.choice(random_valid_hint))  # random, from possible valid hint lst line 56

        elif guess_letter == 'SOLUTION':  # special case for full solution
            print("\nYour solution is: ", hangman_word) # just gives the hangman_word directly

        elif guess_letter == "EASY": # special case for just showing few of the elements in the problem A - C - D
            used_letters.add(random.choice(random_valid_hint))  # adds the hind word directly to used letters
            easy_counter += 1 # bug - in the last use of easy, codes loops back to user input line 80
            if easy_counter == len(hangman_word_letters) - 1:  # easy works fine till the last-1 loop
                break  # then the loop breaks and solves the bug

        else:  # if the input is not a special case, not a alphabet, not has been used again... means invalid entry
            print("\nInvalid entry......try again......\n")
    print(f"\nCongrats, you have guessed the correct word {hangman_word} in {10-lives} tries")


hangman()  # calling the function












