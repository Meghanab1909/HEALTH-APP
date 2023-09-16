from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title('Diet Planner')
root.geometry('700x800')

c = Canvas(root, bg = 'gray16',height = 100,width = 250)
filename = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\GIT - HEALTH APP PROJECT\\output-onlinepngtools.png")
background_label = Label(root,image = filename)
background_label.place(x = 0,y = 0,relwidth = 1, relheight = 1)
c.pack(pady=0)

def home():
    root.destroy()
    os.startfile('start.py')
    
def nextPage():
    root.destroy()
    os.startfile('datasummary.txt')
    
def prevPage():
    root.destroy()
    os.startfile('caloriecounter.py')
    
def Take_input():
    file = open("datasummary.txt","a")
    INPUT = inputtxt.get('1.0','end-1c')
    var = ""
    V = ""
    print(INPUT)
    if(INPUT == '1'):
        file.write("Cuisine: South Indian\n")
        breakfast.insert(END,"Breakfast - 1 cup of coffee without sugar, 2 small idlies/1 cup of wheat upma")
        morning_snack.insert(END,"Morning Snack - 1 fresh fruit and 1 glass of diluted buttermilk")
        lunch.insert(END,"Lunch - 1.5 cups of brown rice or 2 small rotis with 1/2 cup of brown rice, 1 cup of sambhar,\n1 cup of rasam, 1 cup of green beans curry, 1 small roasted papad or appalam")
        afternoon_snack.insert(END,"Afternoon Snack - 1 cup of coffee without sugar and 1/2 cup of dry cereal mix")
        dinner.insert(END,"Dinner - 1/2 cup of brown rice, 1 cup of chick peas, 1 cup of spinach curry and 250g of panfried chicken\n/fish or 1 boiled egg")
        snack.insert(END,"Night Snack - 1 fruit\nExercise properly and try to have a balanced lifestyle")
        var = "Breakfast - 1 cup of coffee without sugar, 2 small idlies/1 cup of wheat upma\nMorning Snack - 1 fresh fruit and 1 glass of diluted buttermilk\nLunch - 1.5 cups of brown rice or 2 small rotis with 1/2 cup of brown rice, 1 cup of sambhar,1 cup of rasam, 1 cup of green beans curry, 1 small roasted papad or appalam\nAfternoon Snack - 1 cup of coffee without sugar and 1/2 cup of dry cereal mix\nDinner - 1/2 cup of brown rice, 1 cup of chick peas, 1 cup of spinach curry and 1/2 cup of pan fried chicken/fish or 1 boiled egg\nSnack - 1 fruit\nExercise properly and try to have a balanced lifestyle"
    elif(INPUT == '2'):
        file.write("Cuisine: North Indian\n")
        breakfast.insert(END,'Breakfast - 1 cup of tea without sugar, 2 whole bread toast')
        morning_snack.insert(END,'Morning Snack - 1 fresh fruit and 1 glass of diluted buttermilk')
        lunch.insert(END,'Lunch - 2 rotis without ghee/oil, 1/2 cup of spinach curry, 1 cup of rajma, 1/4 cup of baked or panfried\nfish/chicken or boiled egg, 1 roasted papad')
        afternoon_snack.insert(END,'Afternoon Snack - 1 cup of tea without sugar and 1/4 cup of fresh fruits')
        dinner.insert(END,'Dinner - 2 rotis without ghee, 1/2 cup of chick peas, 1 cup of cauliflower curry, 1/4 cup of panfried fish\n/chicken or 1 boiled egg, 1/2 cup of yoghurt')
        snack.insert(END,'Night Snack - 1 fruit\nExercise properly and try to have a balanced lifestyle')
        var = "Breakfast - 1 cup of tea without sugar, 2 whole bread toast\nLunch - 2 rotis without ghee/oil, 1/2 cup of spinach curry, 1 cup of rajma, 1/4 cup of baked or panfried fish/chicken or boiled egg, 1 roasted papad\nAfternoon Snack - 1 cup of tea without sugar and 1/4 cup of fresh fruits\nDinner - 2 rotis without ghee, 1/2 cup of chick peas, 1 cup of cauliflower curry, 1/4 cup of pan fried fish/chicken or 1 boiled egg, 1/2 cup of yoghurt\nSnack - 1 fruit\nExercise properly and try to have a balanced lifestyle"
    elif(INPUT == '3'):
        file.write("Cuisine: Chinese\n")
        breakfast.insert(END,'Breakfast - 1 egg, 200ml of banana yoghurt')
        morning_snack.insert(END,'Morning Snack - Fresh Fruit/Backery Buns/Peanuts/Soy Milk')
        lunch.insert(END,'Lunch - 1 cucumber, 300g of panfried chicken with olive oil')
        afternoon_snack.insert(END,'Afternoon Snack - Sweet Potato Snacks/Dry Fruits/Tofu/Rice Rollers/Rice Snacks')
        dinner.insert(END,'Dinner - 300ml of oatmeal, 300g of broccoli and 1 egg')
        snack.insert(END,'Night Snack - 1 Fruit/Yoghurt\nExercise properly and try to have a balanced lifestyle')
        var = "Breakfast - 1 egg, 200ml of banana yoghurt\nMorning Snack - Fresh Fruit/Backery Buns/Peanuts/Soy Milk\nLunch - 1 cucumber, 300g of panfried chicken with olive oil\nDinner - 300ml of oatmeal, 300g of broccoli and 1 egg\nNight Snack - 1 Fruit/Yoghurt\nExercise properly and try to have a balanced lifestyle"
    elif(INPUT == '4'):
        file.write("Cuisine: Italian\n")
        breakfast.insert(END,'Breakfast - Cinnamon Hazelnut Biscotti and a Cappucino')
        morning_snack.insert(END,'Morning Snack - Apple/Banana/Blueberries/Rasberries')
        lunch.insert(END,'Lunch - Panzanella Salad')
        afternoon_snack.insert(END,'Afternoon Snack - Bellissimo Bellinis and Salerno Stuffed Mushrooms/Wheat or Lentil Pasta with lot of \nvegetables')
        dinner.insert(END,'Dinner - Fennel Salad, Garlic Shrimp and Vegetables with Parsely sauce/Caesar Salad/Brushetta')
        snack.insert(END,'Night Snack - Fresh Strawberries\nExercise properly and try to have a balanced lifestyle')
        var = "Breakfast - Cinnamon Hazelnut Biscotti and a Cappucino\nMorning Snack - Apple/Banana/Blueberries/Rassberries\nLunch - Panzanella Salad\nEvening Snack - Bellissimo Bellinis and Salerno Stuffed Mushrooms\nDinner - Fennel Salad, Garlic Shrimp and Vegetables with Parsely sauce or Lentil or Wheat Pasta with a lot of vegetables\nNight Snack - Fresh Strawberries\nExercise properly and try to have a balanced lifestyle"
    elif(INPUT == '5'):
        file.write("Cuisine: General\n")
        breakfast.insert(END,'Breakfast - Cucumber Water, Cup of Oats and Dry Fruits')
        morning_snack.insert(END,'Mid-day Beverage - Green Tea/Black Coffee/Fruit Juice')
        lunch.insert(END,'Lunch - A Cup of Paneer Curry, Dal, Vegetable Salad and 2 rotis')
        afternoon_snack.insert(END,'Afternoon Snack - Cup of Fruits, Glass of Buttermilk, Tea with no sugar and milk')
        dinner.insert(END,'Dinner - A cup of Vegetable Salad, A cup of mixed vegetable curry and dal with 1 roti')
        snack.insert(END,'Night Snack - Fruit Salad/Dry Fruits/Yoghurt\nExercise properly and try to have a balanced lifestyle')
        var = "Breakfast - Cucumber Water, Cup of Oats and Dry Fruits\nMid-day Beverage - Green Tea/Black Coffee/Fruit Juice\nLunch - A Cup of Paneer Curry, Dal, Vegetable Salad and 2 rotis\nAfternoon Snack - Cup of Fruits, Glass of Buttermilk, Tea with no sugar and milk\nDinner - A cup of Vegetable Salad, A cup of mixed vegetable curry and dal with 1 roti\nNight Snack - Fruit Salad/Dry Fruits/Yoghurt\nExercise Properly and Try to have a balanced lifestyle"
    else:
        #Validation No.3
        breakfast.insert(END,'N/A')
        morning_snack.insert(END,'N/A')
        lunch.insert(END,'N/A')
        afternoon_snack.insert(END,'N/A')
        dinner.insert(END,'N/A')
        snack.insert(END,'N/A')
        var = "Invalid Choice"
    file.write("Diet Chart:"+"\n"+var+"\n")
    file.write("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
    
l = Label(text = 'DIET PLANNER',bg = 'white',font = ('Calibri 18'))
l1 = Label(text = 'Choose 1 for South Indian Cuisine',bg = 'white',font = ('Calibri 12'))
l2 = Label(text = 'Choose 2 for North Indian Cuisine',bg = 'white',font = ('Calibri 12'))
l3 = Label(text = 'Choose 3 for Chinese Cuisine',bg = 'white',font = ('Calibri 12'))
l4 = Label(text = 'Choose 4 for Italian Cuisine',bg = 'white',font = ('Calibri 12'))
l5 = Label(text = 'Choose 5 for General Cuisine',bg = 'white',font = ('Calibri 12'))

inputtxt = Text(root, height = 2, width = 15,bg = 'white',font = ('Calibri 12'))
breakfast = Text(root, height = 2, width = 85, bg = 'white',font = ('Calibri 12'))
morning_snack = Text(root, height = 2, width = 85, bg = 'light blue',font = ('Calibri 12'))
lunch = Text(root, height = 2, width = 85, bg = 'white',font = ('Calibri 12'))
afternoon_snack = Text(root, height = 2, width = 85, bg = 'light yellow',font = ('Calibri 12'))
dinner = Text(root, height = 2, width = 85, bg = 'white',font =('Calibri 12'))
snack = Text(root, height = 2, width = 85, bg = 'light pink',font = ('Calibri 12'))

Display = Button(root, height = 2, width = 20, text = 'Display Diet',font = ('Calibri 14'), command = lambda:Take_input())

l.pack()
l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
inputtxt.pack()
Display.pack()
breakfast.pack()
morning_snack.pack()
lunch.pack()
afternoon_snack.pack()
dinner.pack()
snack.pack()

Button(root, text = 'Home',command = home).place(x = 550, y = 100)
Button(root, text = 'Back',command = prevPage).place(x = 600, y = 100)
Button(root, text = 'End',command = nextPage).place(x = 640, y = 100)

mainloop()
