from tkinter import *
from tkinter import ttk

caloriesperladle = Tk()
caloriesperladle.title("Smart Healthy Application")
caloriesperladle.geometry("825x400+600+200")
caloriesperladle.resizable(False,False)
caloriesperladle.config(bg='salmon')

##################################################################

def save() :
    amount_of_rice = amount.get()
    type_of_rice = combo.get()
    Type_of_rice_and_kilocalories = {'brown rice':70,'rice berry':80,'white rice':80,'sticky rice':160,'japanese rice':118,'jasmine rice':80}
    kilocalories = Type_of_rice_and_kilocalories[type_of_rice.lower()] * int(amount_of_rice)
    print(kilocalories)
    Result = Label(rightframe,bg='white',text = "You choose a " + type_of_rice +  ' in ' + str(amount_of_rice) + ' scoops',font = ('Microsoft Yahei UI Light',16) ).place(relx=0.0,rely=0.3)
    Result2 = Label(rightframe,bg='white',text = "that have " + str(kilocalories) +" Kilocalories",font = ('Microsoft Yahei UI Light',16)).place(relx=0.15,rely=0.4)

leftframe = Frame(caloriesperladle,width=350,height=290,bg='white')
leftframe.place(x=50,y=50)

rightframe = Frame(caloriesperladle,width=350,height=290,bg='white')
rightframe.place(x=420,y=50)
    
Head = Label(leftframe,text=' Calories Of Rice In Scoop',fg = '#57a1f8',bg='white',font=('Microsoft Yahei UI Light',16,'bold')).place(relx=0.1,rely=0.02)

amount = IntVar()
amountofriceLabel = Label(leftframe,fg='black',bg='white',text='Amount of rice :',font=('Microsoft Yahei UI Light',13)).place(relx=0.1,rely=0.2)
amountofriceEntry = Entry(leftframe,fg='black',bg='white',width=10,textvariable=amount,font=('Microsoft Yahei UI Light',13))
amountofriceEntry.place(relx=0.5,rely=0.2)
amountofriceEntry.delete('0','end')
scoopLabel = Label(leftframe,fg='black',bg='white',text='scoop',font=('Microsoft Yahei UI Light',13)).place(relx=0.8,rely=0.2)

Typeofrice = Label(leftframe,fg='black',bg='white',text='Type of rice :',font=('Microsoft Yahei UI Light',13)).place(relx=0.1,rely=0.4)
choice = StringVar(value='Type of rice')
combo = ttk.Combobox(leftframe,textvariable=choice,width=12,font=('Microsoft Yahei UI Light',13))
combo['values'] = ("Brown rice","Rice berry","White rice","Sticky rice","Japanese rice","Jasmine rice",)
combo.place(relx=0.47,rely=0.4)

CalculateButton = Button(leftframe,text='Calculate',width=15,command=save).place(relx=0.35,rely=0.6)

HeadResult = Label(rightframe,text='Result',fg = '#57a1f8',bg='white',font=('Microsoft Yahei UI Light',16,'bold')).place(relx=0.4,rely=0.02)



caloriesperladle.mainloop()