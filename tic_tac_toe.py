import random
import tkinter as tk
you_wins=0
computer_wins=0
x_turns = random.choice([True, False])
#x_turns=True
game_over=False

def start_game():
    global x_turns,game_over
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""

    btn1["bg"]="white"
    btn2["bg"]="white"
    btn3["bg"]="white"
    btn4["bg"]="white"
    btn5["bg"]="white"
    btn6["bg"]="white"
    btn7["bg"]="white"
    btn8["bg"]="white"
    btn9["bg"]="white"

    score_label["text"] = "X turn (Your's)" if x_turns else "O turn (Computer)"
    game_over=False

def check_game_status(x_turns):
    if(x_turns):
        check="X"
    else:
        check="O"

    if(btn1["text"]==btn2["text"]==btn3["text"]==check):
        return btn1,btn2,btn3
    if(btn4["text"]==btn5["text"]==btn6["text"]==check):
        return btn4,btn5,btn6
    if(btn7["text"]==btn8["text"]==btn9["text"]==check):
        return btn7,btn8,btn9
    

    if(btn1["text"]==btn4["text"]==btn7["text"]==check):
        return btn1,btn4,btn7
    if(btn2["text"]==btn5["text"]==btn8["text"]==check):
        return btn2,btn5,btn8
    if(btn3["text"]==btn6["text"]==btn9["text"]==check):
        return btn3,btn6,btn9
    
    if(btn1["text"]==btn5["text"]==btn9["text"]==check):
        return btn1,btn5,btn9
    if(btn3["text"]==btn5["text"]==btn7["text"]==check):
        return btn3,btn5,btn7
    
    return None

def check_tie():
    return all(btn["text"] != "" for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9])


def check_click(button):
    global x_turns, game_over, you_wins, computer_wins

    if button["text"] != "" or game_over:
        return

    if x_turns:
        button["text"] = "X"
    else:
        button["text"] = "O"

    btn = check_game_status(x_turns)
    
    if btn:
        btn[0]["bg"] = "green"
        btn[1]["bg"] = "green"
        btn[2]["bg"] = "green"
        if x_turns:
            score_label["text"] = "You win!"
            you_wins += 1
        else:
            score_label["text"] = "Computer wins!"
            computer_wins += 1
        status_label["text"] = "You:{} Computer:{}".format(you_wins, computer_wins)
        game_over = True
    elif check_tie():
        score_label["text"] = "It's a tie!"
        for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
            btn["bg"] = "orange"
        game_over = True
    else:
        x_turns = not x_turns
        score_label["text"] = "X turn (Your's)" if x_turns else "O turn (Computer)"



window=tk.Tk()
window.title("Tic-Tac-Toe Almadrasa")
window.geometry("400x400")

# Score and Status Frame
status_frame = tk.Frame(master=window, height=20)
status_label = tk.Label(master=status_frame, text="You:{} Computer:{}".format(you_wins, computer_wins))
status_label.configure(font=("Times New Roman", 16))
status_label.grid(row=0, column=0, pady=(0, 5))

score_label = tk.Label(master=status_frame)
score_label["text"] = "X turn (Your's)" if x_turns else "O turn (Computer)"
score_label.configure(font=("Times New Roman", 16))
score_label.grid(row=1, column=0, pady=(0, 10))

status_frame.pack()

# Restart Frame
restart_frame = tk.Frame(master=window, height=40)
restart_btn = tk.Button(master=restart_frame, text="Restart", command=start_game, bg="yellow")
restart_btn.configure(font=("Times New Roman", 16))
restart_btn.grid(row=0, column=0, pady=(5, 0))
restart_frame.pack()


grid_frame = tk.Frame(master=window)
btn1=tk.Button(master=grid_frame,width=10,height=5,bg="white",command=lambda:check_click(btn1))
btn2=tk.Button(master=grid_frame,width=10,height=5,bg="white",command=lambda:check_click(btn2))
btn3=tk.Button(master=grid_frame,width=10,height=5,bg="white",command=lambda:check_click(btn3))

btn4=tk.Button(master=grid_frame,width=10,height=5,bg="white",command=lambda:check_click(btn4))
btn5=tk.Button(master=grid_frame,width=10,height=5,bg="white",command=lambda:check_click(btn5))
btn6=tk.Button(master=grid_frame,width=10,height=5,bg="white",command=lambda:check_click(btn6))

btn7=tk.Button(master=grid_frame,width=10,height=5,bg="white",command=lambda:check_click(btn7))
btn8=tk.Button(master=grid_frame,width=10,height=5,bg="white",command=lambda:check_click(btn8))
btn9=tk.Button(master=grid_frame,width=10,height=5,bg="white",command=lambda:check_click(btn9))

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)
grid_frame.pack(side="bottom",pady=20)

window.mainloop()