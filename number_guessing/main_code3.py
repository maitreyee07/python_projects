import random
from random import randint

HARD_LEVEL = 5
EASY_LEVEL = 10


def check(user, computer, turns):
    if user < computer:
        print("too low")
        return turns - 1
    elif user > computer:
        print("too high")
        return turns - 1
    else:
        print("you won")


def set_difficulty():
    choose = input("choose the difficulty level easy or hard : ")
    if choose == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("welcome to the number guesing game:")
    print("think of a number between 1 to 100 ")
    computer = random.randint(0, 100)

    turns = set_difficulty()

    user = 0
    while user != computer:
        user = int(input("Make a guess: "))
        print(f"you have {turns} remaining to guess the number")
        turns = check(user, computer, turns)
        if turns == 0:
            print("you have run out of guesses, you lose")
            return

    print(f" the correct answer is {computer}")


game()

