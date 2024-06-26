from tkinter import *
import random

def empty_space():
    space = 9
    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"] !="":
                space -= 1
    if space == 0:
        return False
    return True

def new_game():
    global player
    player = random.choice(players)
    turnlab.config(text=player+" Turn")
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", bg="#FFFFFF")

def check_winner():
    for r in range(3):
        if buttons[r][0]["text"] == buttons[r][1]["text"] == buttons[r][2]["text"] != "":
            buttons[r][0].config(bg="green")
            buttons[r][1].config(bg="green")
            buttons[r][2].config(bg="green")
            return True

    for c in range(3):
        if buttons[0][c]["text"] == buttons[1][c]["text"] == buttons[2][c]["text"] != "":
            buttons[0][c].config(bg="green")
            buttons[1][c].config(bg="green")
            buttons[2][c].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_space() is False:
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg="yellow")
        return 'Tie'

    return False

def next_turn(r,c):
       global player
       if buttons[r][c]["text"] == "" and check_winner() is False:
           if player == players[0]:
               buttons[r][c]["text"] = player
               if check_winner() is False:
                   player = players[1]
                   turnlab.config(text=player + " Turn")
               elif check_winner() is True:
                   turnlab.config(text=player + " Win")
               elif check_winner() == 'Tie':
                   turnlab.config(text=" Tie !")
           else:
               buttons[r][c]["text"] = player
               if check_winner() is False:
                   player = players[0]
                   turnlab.config(text=player + " Turn")
               elif check_winner() is True:
                   turnlab.config(text=player + " Win")
               elif check_winner() == 'Tie':
                   turnlab.config(text=" Tie !")


buttons=[[0,0,0],[0,0,0],[0,0,0]]
players=['O', 'X']
player=random.choice(players)
root = Tk()
root.title('Tic Tac Toe')
root.geometry("1000x700")
root.resizable(False,False)
root.config(bg='gray')

top_frame = Frame(root, bg="#5D6D73", width=1300, height=250)
top_frame.place(x=0, y=0)

game_title=Label(top_frame, text= "Tic-Tac-Toe with python", font=('',48),bg="#5D6D73",fg="white")
game_title.place(x=135,y=0)

rest_But=Button(top_frame,text="Resart Game",font=('Arial',30),bg="#5D6D73",fg="white", command=new_game)
rest_But.place(x=360,y=95)

turnlab=Label(top_frame, text=player + " Turn", font=('',30),bg="#5D6D73",fg="white")
turnlab.place(x=430,y=180)

but_frame=Frame(root, bg='#FFFFFF', width=500,height=400)
but_frame.place(x=250,y=280)

for r in range(3):
    for c in range(3):
        buttons[r][c]=Button(but_frame, text="",font=('Consolas',48),width=5,height=1, command=lambda ro=r,col=c:next_turn(ro,col))
        buttons[r][c].grid(row=r,column=c)
root.mainloop()