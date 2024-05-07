# this is a game where the player needs to guees a number (1-20) that the computer choose
# inputs: numbers
# outputs: larger, lower, or equal and correct. if equal- returns the number of guesses and the time that take

import random
import time

def main() :
    text()
    [n, num] = num_generator()
    while True:
        while True:
            y_n = start_clock()
            cheat(num)
            if y_n == "y":
                cheat(num)
                start = time.time()
                while True:
                    n = n + 1
                    guess = input("Youre guuess: ")
                    cheat(num)
                    if guess == 'x' :
                        exit()
                        break
                    elif guess == 'n' :
                        main()
                    elif int(guess) == num:
                        correct(n,start)
                        break
                    elif int(guess) > num:
                        biger()
                    else:
                        smaller()
                break
            elif y_n == 'x' :
                break
            elif y_n == 'n' :
                main()
            else:
                continue

        if another_game == 'yes' or another_game == 'n' :
            [n, num] = num_generator()
            continue
        elif another_game == 'nop' or another_game == 'x' :
            exit()
            break 
        else :
            continue



def text() :
    print("\n")
    print(
        "Find the number I choose! (Between 1 to 20) \n\
    \n\
    Your score includes the time t and the number of trials n . For instance: \n\
    n=1, t=1 : score = 100 \n\
    n=3, t=10 : score = 96 \n\
    n=6, t=12 : score = 70 \n\
    n=20, any t : score = 0 \n\
    \n\
    so it's importent to think fast, but luck and strategy are better! \n"
    )
    
def start_clock() :
    y_n = input(
            "Press 'y' when you want to start \n\
    pay attention, the clock will start to run! \n\
    \n"
        )
    return(y_n)


def num_generator() :
    num = random.randrange(1, 21)
    n = 0
    return(n, num)

def score_calc(n, t) :
    score = (round(100 * (1 - ((n - 1) / 19)) * (1 / (1 + (0.004 * t)))))
    return(score)

def correct(n,start) :
    t = time.time() - start
    score = score_calc(n,t)
    print(
          f"Congratulations (: , You are correct! \n\
    Number of trials: {n} \n\
    Time: {t} second \n\
    Score: {score}"
                    )
    
def biger() :
     print(
    f"Sory ): , your guess is BIGER than the number \n\
        try again"
                    )
     
def smaller() :
     print(
    f"Sory ): , your guess is SMALLER than the number \n\
        try again"
                    )
     
def another_game() :
    another_game = input("do you want to play a new game? \n\
                        say 'yes' to continue \n\
                        say 'nop' to exist")
    return(another_game)

def cheat(num) :
    cheat = input()
    if cheat == 's' :
        print("Son of a CHEATER!")
        print(f"{num}")

def exit() :
    print('exit GAME, on you the SHAME')

main()
