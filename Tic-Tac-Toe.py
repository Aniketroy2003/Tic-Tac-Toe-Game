# This is a tic tac toe game

# import tkinter as tk
from tkinter import *
import random

# -----------------------functions------------------------

def player_turn(row,column):
    global player
    if buttons[row][column]['text'] == '' and winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif winner() is True:
                label.config(text=(players[0] + ' wins 😎'))

            elif winner() == 'Tie':
                label.config(text='Its a Tie 😮')

        else:
            if player == players[1]:
                buttons[row][column]['text'] = player

                if winner() is False:
                    player = players[0]
                    label.config(text=(players[0] + ' turn'))

                elif winner() is True:
                    label.config(text=(players[1] + ' wins 😎'))

                elif winner() == 'Tie':
                    label.config(text='Its a Tie 😮')




def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + ' turn')
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='',bg='#F0F0F0')


def winner():

    #------------horizontal match condition-------------
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg='blue')
            buttons[row][1].config(bg='blue')
            buttons[row][2].config(bg='blue')
            return True


    #------------vertical match condition-------------
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg='blue')
            buttons[1][column].config(bg='blue')
            buttons[2][column].config(bg='blue')
            return True


    #------------Diagonal Condition----------------
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='blue')
        buttons[1][1].config(bg='blue')
        buttons[2][2].config(bg='blue')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='blue')
        buttons[1][1].config(bg='blue')
        buttons[2][0].config(bg='blue')
        return True

    #----------Tie condition------------

    elif blank_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="grey")
        return "Tie"

    else:
        return False


def blank_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True




#-----------------------The GUI part-----------------------------

window = Tk()                       # initialising gui window
window.title('Tic-Tac-Toe Game')
players = ['x','o']                  # player selections
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text = player + ' turn',font=('consolas',36))
label.pack(side='top')

reset_button = Button(text='restart', font=('consolas',15), command=new_game)
reset_button.pack(side='top')


frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 20), width=5, height=2,
                                      command= lambda row=row, column=column: player_turn(row, column))
        buttons[row][column].grid(row=row,column=column)


window.mainloop()