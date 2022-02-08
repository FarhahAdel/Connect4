import tkinter as tk
from tkinter import *
from PIL import ImageTk as imgtk
from PIL import Image as imgpl 
from tkinter.ttk import *
from tkinter import messagebox 
import os
from game import *
def alphaBeta():
    master.destroy()
    game(1,int(depthData.get()))

def minMax():
    master.destroy()
    game(0,int(depthData.get()))


def secondPage():
    goBtn.place_forget()
    label.place_forget()
    textbox1.place_forget()
    myPath=os.path.dirname(__file__)
    file2="with"+".png"
    absFile2=os.path.join(myPath,file2)
    file3="without"+".png"
    absFile3=os.path.join(myPath,file3)
    photo1=PhotoImage(file =absFile2)
    photo2=PhotoImage(file = absFile3)
    button1 = tk.Button(master, image=photo1, width=310, command=alphaBeta, bd=0, bg="#ADD8E6")
    button1.place(x=160,y=300)
    button2 = tk.Button(master, image=photo2, width=315, command=minMax, bd=0, bg="#ADD8E6")
    button2.place(x=165,y=400)
    screen.mainloop()
def onGo():
    x=depthData.get()
    if not x:
        messagebox.showerror(title="ERror", message="Please enter depth")
    else:
        secondPage()
master = Tk()
master.title("Start")
screen = Canvas(master, width=600, height=600,bg="#ADD8E6")
screen.pack()
myPath=os.path.dirname(__file__)
file1="connect4"+".png"
absFile=os.path.join(myPath,file1)
i=imgpl.open (absFile).convert("RGB")
image1 = i.resize((150, 150), imgpl.ANTIALIAS)
img = imgtk.PhotoImage(image1)
label1 = tk.Label(image=img)
label1.image = img
label1.place(x=235,y=90)
master.geometry('600x600')
label=tk.Label(master,text="Enter depth",bg="#ADD8E6",font=("monospace",13))
label.pack()
label.place(x=190,y=350)
depthData = tk.StringVar()
textbox1 = tk.Entry(master, width = 15, textvariable = depthData,font=("monospace",13))
textbox1.place(x=290,y=350)
go="go"+".png"
absFile1=os.path.join(myPath,go)
photo1=PhotoImage(file =absFile1)
goBtn = tk.Button(master, image=photo1, width=310, command=onGo, bd=0, bg="#ADD8E6")
goBtn.place(x=150,y=400)
master.mainloop()