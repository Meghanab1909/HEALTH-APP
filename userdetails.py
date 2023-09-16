import tkinter as tk
from tkinter import *
from tkinter import ttk
import os

root = tk.Tk()

root.geometry('700x800')
root.title('Userdetails')

bg = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\GIT - HEALTH APP PROJECT\\e3216b575d5e92031eaf5c1a067f9d31-cpy.png")
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)
                
name_var = tk.StringVar()
age_var = tk.StringVar()
gen_var = tk.StringVar()

def submit():
    name = name_var.get()
    age = age_var.get()
    gender = gen_var.get()

    show = ""

    file = open("datasummary.txt", "a")
    file.write("User Details \n")
    #Validation No.1
    if(name.isdigit() == True or age.isdigit() == False or age[0] == '-'):
        show = "Invalid entries, entered data cannot be displayed"
        if(name.isdigit() == True and age.isdigit() == True and age[0] != '-'):
            file.write("Name: N/A \n")
            file.write("Age: "+age+"\n")
            show = 'Name: N/A \n'+'Age: '+age+'\n Gender: '+gender
        elif(name.isdigit() == False and age.isdigit() == False or age[0] == '-'):
            file.write("Name: "+name+"\n")
            file.write("Age: N/A \n")
            show = 'Name: '+name+'\n Age: N/A'+'\n Gender: '+gender
        elif(name.isdigit() == True and age.isdigit() == False or age[0] == '-'):
            file.write("Name: N/A \n")
            file.write("Age: N/A \n")
            show = 'Name: N/A '+'\n Age: N/A'+'\n Gender: '+gender
    else:
        show = 'Name: '+name+'\n Age: '+age+'\n Gender: '+gender
        file.write("Name: "+name+"\n")
        file.write("Age: "+age+"\n")
        
    file.write("Gender: "+gender+"\n")
    file.write("\n")
    
    name_var.set("")
    age_var.set(" ")
    gen_var.set("")

    label.config(text = show)
        
def home():
    root.destroy()
    os.startfile('start.py')

def nextpage():
    root.destroy()
    os.startfile('bmicalculator.py')

def end():
    root.destroy()
    os.startfile('datasummary.txt')

title = tk.Label(root, text = 'USERDETAILS',font = ('Calibri 20'))
nameLabel = tk.Label(root, text = 'Name',font = ('Calibri 16'))
nameEntry = tk.Entry(root, textvariable = name_var, font = ('Calibri 16'))

ageLabel = tk.Label(root, text = 'Age',font = ('Calibri 16'))
ageEntry = tk.Entry(root, textvariable = age_var,font = ('Calibri 16'))

genderLabel = tk.Label(root, text = 'Gender',font = ('Calibri 16')).grid(row = 3, column = 0)

genbox = ttk.Combobox(root, width = 18, textvariable = gen_var, font = ('Calibri 16'))
genbox['values'] = ('Male',
                    'Female')
genbox.grid(row = 3, column = 1)
genbox.current()

submit = tk.Button(root, text = 'Submit', command = submit)

home = tk.Button(root, text = 'Home',command = home)

nextpage = tk.Button(root, text = 'Next',command = nextpage)

end = tk.Button(root, text = 'End',command = end)

label = tk.Label(root, text = "",font = ('Calibri 16'))

title.grid(row = 0, column = 1)
nameLabel.grid(row = 1, column = 0)
nameEntry.grid(row = 1, column = 1)
ageLabel.grid(row = 2, column = 0)
ageEntry.grid(row = 2, column = 1)
submit.grid(row = 6, column = 1)
label.grid(row = 8, column = 1)
home.place(x = 550, y = 0)
nextpage.place(x = 600,y = 0)
end.place(x = 642, y = 0)
root.mainloop()
