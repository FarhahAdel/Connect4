import tkinter as tk
from tkinter import *

from tkinter.ttk import *
import os

def playAgain(root):
    root.destroy()
    import home

def displayScores(aiScore,playerScore):

    master = Tk()
    master.title("End")
    screen = Canvas(master, width=600, height=600,bg="#ADD8E6")
    screen.pack()
    
    ai_score=tk.Label(master,text="AI Score:"+str(aiScore),font=("monospace",30),bg="#ADD8E6")
    ai_score.pack()
    ai_score.place(x=200,y=200)
    player_score=tk.Label(master,text="Player Score:"+str(playerScore),font=("monospace",30),bg="#ADD8E6")
    player_score.pack()
    player_score.place(x=200,y=270)
    myPath=os.path.dirname(__file__)
    file="play"+".png"
    absFile=os.path.join(myPath,file)
    print(absFile)
    photo1=PhotoImage(file =absFile)
    button1 = tk.Button(master, image=photo1, width=310, command=lambda:playAgain(master), bd=0, bg="#ADD8E6")
    button1.place(x=150,y=450)
    if aiScore<playerScore:
        winner=tk.Label(master,text="Player 1 wins!!",font=("monospace",30),bg="#ADD8E6",fg='red')
    

    else:
       winner=tk.Label(master,text="Player 2 wins!!",font=("monospace",30),bg="#ADD8E6",fg='yellow')
    
    
    winner.pack()
    winner.place(x=200,y=350)
    screen.mainloop()