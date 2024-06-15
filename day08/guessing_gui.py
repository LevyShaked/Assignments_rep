import random
import time
import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title('Multiple Buttons Example')

input_window = None  
shhhh_button = None

def get_input():
    global input_window

    def on_submit():
        nonlocal user_input
        user_input = entry.get()
        input_window.destroy()

    if input_window is not None and tk.Toplevel.winfo_exists(input_window):
        input_window.destroy()

    input_window = tk.Toplevel(app)
    input_window.title("Input Window")

    tk.Label(input_window, text="Enter your guess:").pack()

    entry = tk.Entry(input_window)
    entry.pack()

    submit_button = tk.Button(input_window, text="Submit", command=on_submit)
    submit_button.pack()

    user_input = None
    input_window.wait_window()

    return user_input

def create_popup(num):
    messagebox.showinfo("Sun of a CHEATER", str(num))

def start_again():
    main()

def main():
    global shhhh_button

    if shhhh_button is not None:
        shhhh_button.destroy()

    counter, num = num_generator()
    shhhh_button = tk.Button(app, text='Shhhh', width=25, command=lambda: create_popup(num))
    shhhh_button.pack()
    yes_or_else_loopa(counter, num)

def game(counter, num):
    start = time.time()
    while True:
        guess = get_input()
        if guess == "s":
            cheat(num)
            continue
        counter += 1
        if guess == "x":
            exit_fun()
            return
        elif guess == "n":
            another_game_loopa(counter, num)
        elif int(guess) == num:
            correct(counter, start)
            another_game_loopa(counter, num)
        elif int(guess) > num:
            bigger()
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
        return
    else:
        yes_or_else_loopa(counter, num)

def another_game_loopa(counter, num):
    another_game = another_game_fun()
    if another_game == "yes":
        main()
    elif another_game == "nop" or another_game == "x":
        exit_fun()
        return
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
    Your score includes the time t and the number of trials counter. For instance: \n\
    counter=1, t=1 : score = 100 \n\
    counter=3, t=10 : score = 96 \n\
    counter=6, t=12 : score = 70 \n\
    counter=20, any t : score = 0 \n\
    \n\
so it's important to think fast, but luck and strategy are better! \n"
    )


def start_clock():
    while True:
        response = messagebox.askyesno(
            "Start Clock", 
            "Press 'Yes' when you want to start.\n\n"
            "Pay attention, the clock will start to run!"
        )
        if response:
            return "y"
        else:
            exit()

def num_generator():
    num = random.randrange(1, 21)
    counter = 0
    return counter, num

def score_calc(counter, t):
    score = round(100 * (1 - ((counter - 1) / 19)) * (1 / (1 + (0.004 * t))))
    return score

def correct(counter, start):
    t = time.time() - start
    score = score_calc(counter, t)
    print(
        f"Congratulations (: , You are correct! \n\
    Number of trials: {counter} \n\
    Time: {t} second \n\
    Score: {score}"
    )

def bigger():
    print(
        f"Sorry ): , your guess is BIGGER than the number \n\
        try again"
    )

def smaller():
    print(
        f"Sorry ): , your guess is SMALLER than the number \n\
        try again"
    )

def another_game_fun():
    another_game = input(
        "do you want to play a new game? \n\
say 'yes' to continue \n\
say 'nop' to exit \n"
    )
    return another_game

def cheat(num):
    print("Son of a CHEATER!")
    print(f"{num} \n")

def exit_fun():
    print("exit GAME, on you the SHAME")
    app.quit()
    exit()

button1 = tk.Button(app, text='Exit Game', width=25, command=exit_fun)
button1.pack()

button2 = tk.Button(app, text='Start Again', width=25, command=start_again)
button2.pack()

text()
main()
app.mainloop()