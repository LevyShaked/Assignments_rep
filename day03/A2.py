# this is a game where the player needs to guees a number (1-20) that the computer choose
# inputs: numbers
# outputs: larger, lower, or equal and correct. if equal- returns the number of guesses and the time that take

import random
import time

def main():
    (counter, num) = num_generator()
    yes_or_else_loopa(counter, num)


def game(counter, num):
    start = time.time()
    while True:
        guess = input("Youre guuess: ")
        if guess == "s":
            cheat(num)
            continue
        counter += 1
        if guess == "x":
            exit_fun()
            exit()
        elif guess == "n":
            another_game_loopa(counter, num)
        elif int(guess) == num:
            correct(counter, start)
            another_game_loopa(counter, num)
        elif int(guess) > num:
            biger()
        elif int(guess) < num:
            smaller()
        else:
            game(counter, num)


def yes_or_else_loopa(counter, num):
    yes_or_else = start_clock()
    if yes_or_else == "y":
        game(counter, num)
    elif yes_or_else == "s":
        cheat(num)
        yes_or_else_loopa(counter, num)
    elif yes_or_else == "n":
        another_game_loopa(counter, num)
    elif yes_or_else == "x":
        exit_fun()
        exit()
    else:
        yes_or_else_loopa(counter, num)


def another_game_loopa(counter, num):
    another_game = another_game_fun()
    if another_game == "yes":
        main()
    elif another_game == "nop" or another_game == "x":
        exit_fun()
        exit()
    elif another_game == "s":
        cheat(num)
        another_game_loopa(counter, num)
    elif another_game == "n":
        another_game_loopa(counter, num)
    else:
        another_game_loopa(counter, num)


def text():
    print("\n")
    print(
        "Find the number I choose! (Between 1 to 20) \n\
    \n\
    Your score includes the time t and the number of trials counter . For instance: \n\
    counter=1, t=1 : score = 100 \n\
    counter=3, t=10 : score = 96 \n\
    counter=6, t=12 : score = 70 \n\
    counter=20, any t : score = 0 \n\
    \n\
so it's importent to think fast, but luck and strategy are better! \n"
    )


def start_clock():
    yes_or_else = input(
        "Press 'y' when you want to start \n\
pay attention, the clock will start to run! \n\
\n"
    )
    return yes_or_else


def num_generator():
    num = random.randrange(1, 21)
    counter = 0
    return (counter, num)


def score_calc(counter, t):
    score = round(100 * (1 - ((counter - 1) / 19)) * (1 / (1 + (0.004 * t))))
    return score


def correct(counter, start):
    t = time.time() - start
    score = score_calc(counter, t)
    print(
        f"Congrajulations (: , You are correct! \n\
    Number of trials: {counter} \n\
    Time: {t} second \n\
    Score: {score}"
    )


def biger():
    print(
        f"Sory ): , your guess is BIGER than the number \n\
        try again"
    )


def smaller():
    print(
        f"Sory ): , your guess is SMALLER than the number \n\
        try again"
    )


def another_game_fun():
    another_game = input(
        "do you want to play a new game? \n\
say 'yes' to continue \n\
say 'nop' to exist \n"
    )
    return another_game


def cheat(num):

    print("Son of a CHEATER!")
    print(f"{num} \n")


def exit_fun():
    print("exit GAME, on you the SHAME")
    exit()


# text()
# main()
