# this is a game where the player needs to guees a number (1-20) that i chose (12)
# inputs: numbers
# outputs: larger, lower, or equal and correct. if equal- returns the number of giesses and the time that take

import random 
import time

num = random.randrange(1, 21)
num = 12
n = 0
t = 0
print('\n')
print("Find the number I choose! (Between 1 to 20) \n\
\n\
Your score includes the time t and the number of trials n . For instance: \n\
n=1, t=1 : score = 100 \n\
n=3, t=10 : score = 96 \n\
n=6, t=12 : score = 70 \n\
n=20, any t : score = 0 \n\
\n\
so it's importent to think fast, but luck and strategy are better! \n")

while True :
    y_n = input('Press y if you want to start \n\
(pay attention, the clock will start to run!) \n\
\n')
    if y_n == 'y' :
        start = time.time()
        while True :
            n = n + 1
            guess = input("Youre guuess: ")
            if int(guess) == num :
                t = time.time() - start
                score = round(100*(1-((n-1)/19))*(1/(1+(0.004*t))))
                print(f"Congratulations (: , You are correct! \n\
Number of trials: {n} \n\
Time: {t} second \n\
Score: {score}")
                break
            elif int(guess) > num :
                print(f"Sory ): , your guess is biger than the number \n\
try again")
            else :
                print(f"Sory ): , your guess is smaller than the number. \n\
try again")
        break
    else :
        continue



        



