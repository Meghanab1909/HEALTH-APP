import tkinter
from tkinter import messagebox
import tkinter as ttk
from tkinter import *
import os

root = tkinter.Tk()
root.title("Calorie Counter")
root.geometry('700x800')

c = Canvas(root, bg = 'white',height = 25, width = 50)
filename = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\GIT - HEALTH APP PROJECT\\ng-hacks-to-calories-in-check-feat-1.png")
background_label = Label(root, image = filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
c.pack()

def nextPage():
   root.destroy()
   os.startfile('dietplanner.py')
def prevPage():
   root.destroy()
   os.startfile('bmicalculator.py')
def home():
   root.destroy()
   os.startfile('start.py')
def end():
   root.destroy()
   os.startfile('datasummary.txt')
   
tkinter.Label(root, text = 'CALORIE COUNTER',font = ('Calibri 20')).pack()
# Add a grid
mainframe = tkinter.Frame(root)
#mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
 
# Create a Tkinter variable
tkvar = tkinter.StringVar(root)

# Dictionary with options
choices = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10}

#Breakfast
bchoices = {'Pongal':140,'Poori':107,'Upma':80,'Idly':40,'Dosa':105,'Ragi Dosa':80,
            'Rava Dosa':110,'Idiyapam':57,'Puttu':150,'Poha':241,'Masala Omelet':225,
            'Oats':102,'Fruit Salad':70,'Vegetable Sandwich':100,'Parantha Curd':141,
            'Cereal':110,'Pancakes':227,'Waffles':291,'French Toast':229,'Scrambled Eggs':148,'No Item':0}
tkvar.set('Select') # set the default option
 
popupMenu = tkinter.OptionMenu(mainframe, tkvar, *bchoices)
tkinter.Label(mainframe, text = "BREAKFAST",font = ('Calibri 17')).grid(row = 1, column = 1)
tkinter.Label(mainframe, text="Choose Item",font = ('Calibri 12')).grid(row = 2, column = 1)
popupMenu.grid(row = 2, column =2)

tkvar1 = tkinter.IntVar(root)
tkvar1.set(1) #setting the default value

popupMenu = tkinter.OptionMenu(mainframe, tkvar1, *choices)
tkinter.Label(mainframe, text = "Choose Quantity",font = ('Calibri 12')).grid(row = 3,column = 1)
popupMenu.grid(row = 3, column = 2)

#Lunch
tkvar2 = tkinter.StringVar(root)
lchoices = {'South Indian Thali':450,'Tamarind Rice':271,'Idiyapam':170,'Fish Curry + Rice or Roti':430,
            'Prawn Curry + Rice or Roti':425,'Lemon Rice':300,'Appam + Stew':372,'Malabar Parantha Curry':550,'Chicken Curry + Rice or Roti':310,
            'Rasam Rice':133,'Tomato Rice':280,'Sambar Rice':285,'Dal + Rice or Roti':175,'Parantha Butter':216,
            'Butter Chicken + Rice or Roti':460,'Dal Makhani + Rice or Roti':400,'Pasta':220,'Salad':100,'Roasted Chicken':192,
            'Pan Fried Fish':200,'No Item':0}
tkvar2.set('Select')

popupMenu = tkinter.OptionMenu(mainframe, tkvar2, *lchoices)
tkinter.Label(mainframe,text = '_____________________________________________________________').grid(row = 4, column = 1)
tkinter.Label(mainframe, text = "LUNCH",font = ('Calibri 17')).grid(row = 5, column = 1)
tkinter.Label(mainframe, text = "Choose Item",font = ('Calibri 12')).grid(row = 6, column = 1)
popupMenu.grid(row= 6, column = 2)

tkvar3 = tkinter.IntVar(root)
popupMenu = tkinter.OptionMenu(mainframe, tkvar3, *choices)
tkinter.Label(mainframe, text = "Choose Quantity",font = ('Calibri 12')).grid(row = 7,column = 1)
popupMenu.grid(row = 7, column = 2)
tkvar3.set(1)

#Snacks
tkvar4 = tkinter.StringVar(root)
schoices = {'Chocolate Covered Strawberries':57,'Dry Fruits':76,'Peanut Butter and Jelly Sandwich':390,
            'Apple + Peanut Butter':283,'Potato Chips':152,'French Fries':140,'Candy/Chocolates':235,
            'Mixed Fruits':80,'Samosa':262,'Kachori':195,'Vada Pav':197,'Chaat':147,'Nachos + Cheese':306,
            'Biscuits':60,'Yogurt':60,'No item':0}
tkvar4.set('Select')

popupMenu = tkinter.OptionMenu(mainframe, tkvar4, *schoices)
tkinter.Label(mainframe, text = '_____________________________________________________________').grid(row = 8, column = 1)
tkinter.Label(mainframe, text = "SNACK",font = ('Calibri 17')).grid(row = 9, column = 1)
tkinter.Label(mainframe, text = "Choose Item",font = ('Calibri 12')).grid(row = 10, column = 1)
popupMenu.grid(row = 10, column = 2)

tkvar5 = tkinter.IntVar(root)
popupMenu = tkinter.OptionMenu(mainframe, tkvar5, *choices)
tkinter.Label(mainframe, text = "Choose Quantity",font = ('Calibri 12')).grid(row = 11, column = 1)
popupMenu.grid(row = 11, column = 2)
tkvar5.set(1)

#Dinner
tkvar6 = tkinter.StringVar(root)
dchoices = {'Parantha Curd':260,'Paneer Butter Masala + Rice or Roti':450,'Naan':262,
            'Butter Chicken + Rice or Roti':460,'Dal Makhani + Rice or Roti':300,'Pasta':220,'Pulao':359,
            'Biriyani':448,'Fried Rice':163,'Manchuria':183.4,'Momos':228,
            'Fish Curry + Rice or Roti':430,'Prawn Curry + Rice or Roti':425,'Lemon Rice':300,'Appam':170,
            'Chicken Curry':260,'Rasam Rice':133,'Tomato Rice':280,'Sambar Rice':285,
            'Dal + Rice or Roti':175,'Chole Batura':427,'Salad':100,'Roasted Chicken':192,
            'Pan Fried Fish':200,'No Item':0}
tkvar6.set('Select')

popupMenu = tkinter.OptionMenu(mainframe, tkvar6, *dchoices)
tkinter.Label(mainframe, text = '_____________________________________________________________').grid(row = 12, column = 1)
tkinter.Label(mainframe, text = 'DINNER',font = ('Calibri 17')).grid(row = 13, column = 1)
tkinter.Label(mainframe, text = "Choose Item",font = ('Calibri 12')).grid(row = 14, column = 1)
popupMenu.grid(row = 14, column = 2)

tkvar7 = tkinter.IntVar(root)
popupMenu = tkinter.OptionMenu(mainframe, tkvar7, *choices)
tkinter.Label(mainframe, text = "Choose Quantity",font = ('Calibri 12')).grid(row = 15, column = 1)
popupMenu.grid(row = 15, column = 2)
tkvar7.set(1)

# on change dropdown value
def change_dropdown(*args):
   '''
    v = tkvar.get()
    print(v)
    print(tkvar1.get())
    print("calories for breakfast",bchoices[v])

    breakfast = tkvar.get()
    print("calories for breakfast",bchoices[breakfast])

    lunch=tkvar2.get()
    print("calories for breakfast",lchoices[lunch])
   
    res = breakfast+lunch
    print(res)
    '''

def calc():
    breakfast = tkvar.get()
    quanB = tkvar1.get()
    breakfast_calories = bchoices[breakfast] * choices[quanB]

    lunch=tkvar2.get()
    quanL = tkvar3.get()
    lunch_calories = lchoices[lunch] * choices[quanL]
    
    snack = tkvar4.get()
    quanS = tkvar5.get()
    snack_calories = schoices[snack] * choices[quanS]
    
    dinner = tkvar6.get()
    quanD = tkvar7.get()
    dinner_calories = dchoices[dinner] * choices[quanD]
        
    total = Label(root, text = "Breakfast = "+str(breakfast_calories)+", Lunch = "+str(lunch_calories)+", Snack = "+str(snack_calories)+", Dinner = "+str(dinner_calories),font = ('Calibri 12')).pack()
    
    res = (breakfast_calories + lunch_calories + snack_calories + dinner_calories)
    R = Label(root, text = "Total Calories Consumed: "+str(res),font = ('Calibri 12')).pack()
    label.configure(text=res)
    
    file = open("datasummary.txt","a")  
    file.write("Total Calories Consumed: "+str(res)+"\n")
    file.write("\n")
Button(root, text = 'Calories Consumed',font = ('Calibri 14'), command = calc).pack()
#label = Label(mainframe).grid(row=16,column=2,pady=20)
label = Label(root)
#label.pack(pady = 20)
#label.grid(row=1,column=5,pady=20)
# link function to change dropdown
#tkvar.trace('w', change_dropdown)'''


Button(root, text = 'Home',command = home).place(x = 500, y = 0)
Button(root, text = 'Back',command = prevPage).place(x = 550, y = 0)
Button(root, text = 'Next',command = nextPage).place(x = 592, y = 0)
Button(root, text = 'End',command = end).place(x = 635, y = 0)
root.mainloop()





