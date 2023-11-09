import tkinter as tk
import random

won, Lose, Draw = 0, 0, 0
dic = {"Rock": "🪨", "Paper": "📜", "Scissors": "✂️"}
l = list(dic.keys())

def play_round(user_choice):
    global won, Lose, Draw
    computer_choice = random.choice(l)

    user_choose.config(text=f" {dic[user_choice]}")
    computer_choose.config(text=f" {dic[computer_choice]}")

    if user_choice == computer_choice:
        Draw += 1
        result_label.config(text=f"Both players selected {user_choice}. It's a tie!", fg="blue")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        won += 1
        result_label.config(text=f"You win! {dic[user_choice]} beats {dic[computer_choice]}", fg="green")
    else:
        Lose += 1
        result_label.config(text=f"You lose! {dic[computer_choice]} beats {dic[user_choice]}", fg="red")

    update_score()
    animate_result_label()

def update_score():
    score_label.config(text=f'Wins: {won} | Losses: {Lose} | Draws: {Draw}')

def on_button_click(user_choice):
    play_round(user_choice)

def animate_result_label():
    result_label.config(bg="lightyellow")
    app.after(500, lambda: result_label.config(bg=app.cget("bg")))

def reset_game():
    global won, Lose, Draw
    won, Lose, Draw = 0, 0, 0
    update_score()
    result_label.config(text="", fg="black")

app = tk.Tk()
app.title("Rock, Paper, Scissors Game")
app.configure(bg="lightblue")
app.geometry('400x400')

user_label = tk.Label(app, text='User: ', font=('Arial', 12, 'bold'), fg='black', bg='pink').place(x=50, y=100)
user_choose = tk.Label(app, text="", font=('Arial', 12, 'bold'), fg='black', bg='pink')
user_choose.place(x=150, y=100)

computer_label = tk.Label(app, text='Computer: ', font=('Arial', 12, 'bold'), fg='black', bg='pink').place(x=50, y=150)
computer_choose = tk.Label(app, text="", font=('Arial', 12, 'bold'), fg='black', bg='pink')
computer_choose.place(x=180, y=150)

# Labels
result_label = tk.Label(app, text="", font=("Arial", 12,'bold'), fg="black")
result_label.pack(pady=10)

# Score label
score_label = tk.Label(app, text="", font=("Arial", 12,'bold'), fg="black")
score_label.pack(pady=10)

# Buttons
rock_button = tk.Button(app, text="Rock", command=lambda: on_button_click("Rock"),font=('Arial',10,'bold'),bg='Red')
rock_button.pack(side=tk.LEFT, padx=10)
paper_button = tk.Button(app, text="Paper", command=lambda: on_button_click("Paper"),font=('Arial',10,'bold'),bg='Green')
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button = tk.Button(app, text="Scissors", command=lambda: on_button_click("Scissors"),font=('Arial',10,'bold'),bg='teal')
scissors_button.pack(side=tk.LEFT, padx=10)

# Reset button
reset_button = tk.Button(app, text="Reset", command=reset_game,font=('Arial',10,'bold'),bg='yellow')
reset_button.pack(side=tk.LEFT, padx=10)

app.mainloop()
