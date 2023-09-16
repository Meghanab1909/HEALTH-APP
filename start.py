from tkinter import Tk
from tkinter.ttk import Button
from tkinter import *
import os

root = Tk()
root.title('Main Window')
root.geometry('700x800')

c = Canvas(root, bg = 'gray16',height = 150, width = 150)
filename = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\GIT - HEALTH APP PROJECT\\Center-for-Family-Medicine-Sherman-Texas-True-Benefits-Of-A-Health-Weight-Understanding-BMI.png")
background_label = Label(root, image = filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
c.pack()

label = Label(root, text = 'BMI, CALORIE COUNTER, DIET PLANNER',font = ('Calibri 20'),bg = "white").place(x = 150, y = 300)

def Next():
    root.destroy()
    os.startfile('userdetails.py')

open_bmi = Button(root, text = '                    START                    ',font = ('Calibri 20'),command = Next,bg = "white").place(x = 220, y = 350)

root.mainloop()
