'''
BMI Index
'''
#Importing the required libraries
from tkinter import *
from tkinter import messagebox
import tkinter
import tkinter as tk
from tkinter import ttk
import os

#Creating an instance of tkinter frame or window
#BMI Calculator
window = tkinter.Tk()
window.title('BMI CALCULATOR')
window.geometry('700x800')

c = Canvas(window, bg = 'gray16',height = 200, width = 200)
filename = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\GIT - HEALTH APP PROJECT\\IBW.png")
background_label = Label(window, image = filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
c.pack()

def nextPage():
    window.destroy()
    os.startfile('caloriecounter.py')

def home():
    window.destroy()
    os.startfile('start.py')

def prevPage():
    window.destroy()
    os.startfile('userdetails.py')

def end():
    window.destroy()
    os.startfile('datasummary.txt')
    
#Defining a function for calculating the BMI
def cal_BMI():
    E1 = e1.get()    
    E2 = e2.get()
    BMI = 1.0
    
    file = open("datasummary.txt","a")
    
    flag = 0

    #Validation No.2
    weight = E1.replace('.','',1).isdigit()
    height = E2.replace('.','',1).isdigit()
    
    if(weight is False or height is False):
        if(E1.isdigit() is False and E2.isdigit() is True):
            file.write("Weight: N/A \n")
            file.write("Height: "+E2+"m \n")
        elif(E2.isdigit() is False and E1.isdigit() is True):
            file.write("Weight: "+E1+" kg \n")
            file.write("Height: N/A \n")
        elif(E1.isalpha() is True and E2.isalpha() is True):
            file.write("Weight: N/A \n")
            file.write("Height: N/A \n")
        else:
            if(weight is True and height is False):
                file.write("Weight: "+E1+"kg \n")
                file.write("Height: N/A \n")
            else:
                file.write("Weight: N/A \n")
                file.write("Height: "+E2+"m \n")
        file.write("BMI: N/A \n")
        res = "BMI: N/A; Cannot be calculated due to invalid entry"
    else:
        BMI = float(E1) / (float(E2) * float(E2))
        file.write("Weight: "+E1+" kg \n")
        file.write("Height: "+E2+" m \n")
        file.write("BMI: "+str(int(BMI))+" kg/m2 \n")
        if(BMI < 18.5):
            bmi = "Health Risk - Underweight"
            file.write("Health Risk: Underweight \n")
        elif(BMI >= 18.5 and BMI <= 24.9):
            bmi = "Health Risk - Normal"
            file.write("Health Risk: Normal \n")
        elif(BMI >= 25 and BMI <= 29.9):
            bmi = "Health Risk - Overweight"
            file.write("Health Risk: Overweight \n")
        elif(BMI >= 30 and BMI <= 34.9):
            bmi = "Health Risk - Obese"
            file.write("Health Risk: Obese \n")
        else:
            bmi = "Health Risk - Extremely Obese"
            file.write("Health Risk: Extremely Obese \n")
        res = "BMI:"+str(int(BMI))+" ; "+bmi
    file.write("\n")
    label.config(text = res)

#Creating an Entry Widget
Label(window,text = "         BMI         ",font = ('Calibri 21')).pack()
Label(window, text = "        Body Mass Index         ",font = ('Calibri 11')).pack()
Label(window,text = 'Enter weight in kg:', font = ('Calibri 15')).pack()
e1 = Entry(window,width = 35,font = ('Calibri 12'))
e1.pack()
Label(window,text = 'Enter height in m', font = ('Calibri 15')).pack()
e2 = Entry(window, width = 35,font = ('Calibri 12'))
e2.pack()
'''Label(window,text = 'Select Gender',font = ('Calibri 15')).pack()
v = IntVar()
Radiobutton(window, text='Male   ', font = ('Calibri 12'),variable=v, value=1).pack()
Radiobutton(window, text='Female', font = ('Calibri 12'),variable=v, value=2).pack()'''
Button(window, text = "Calculate BMI",font = ('Calibri 15'),command = cal_BMI).pack()
label = Label(window, text = "",font = ('Calibri 15')) 
label.pack()
home = Button(window, text = 'Home', command = home).place(x = 500, y = 70)
prev = Button(window, text = 'Back',command = prevPage).place(x = 550, y = 70)
nxt = Button(window, text = 'Next',command = nextPage).place(x = 592, y = 70)
end = Button(window, text = 'End',command = end).place(x = 635, y = 70)
window.mainloop()


    
