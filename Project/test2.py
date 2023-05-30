from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import filedialog
import requests
import os
import tkinter.messagebox

root = Tk()
root.title("Smart Healthy Application")
root.config(bg="salmon")

leftframe = Frame(root,width=400,height=200,bg='white')
leftframe.place(x=19,y=55)

underleftframe = Frame(root,width=400,height=200,bg='white')
underleftframe.place(x=19,y=270)

rightframe = Frame(root,width=400,height=200,bg='white')
rightframe.place(x=500,y=55)

underrightframe = Frame(root,width=400,height=200,bg='white')
underrightframe.place(x=500,y=270)

#Resolution
root.geometry("925x500+300+200") #res
Welcome = Label(root,text="Welcome To Smart Health Application",bg='skyblue',font=('TH Sarabun New',23,'bold')).place(x=270,y=0)
root.resizable(False,False)

#Menu #เพิ่มค่าเกณฑ์มาตรฐาน
def clickedHowtouse() :
    tkinter.messagebox.showinfo("รายละเอียดโปรแกรม",'1.ใส่อายุ น้ำหนักและส่วนสูง\n2.เลือกฟังก์ชันที่ต้องการใช้')

def clickedshowdeveloper() :
    tkinter.messagebox.showinfo("ผู้พัฒนา","1.กฤตภาส แจ่มวิลัยพันธุ์\n2.พัชรพล แก้วเนิน\n3.ศุภวิชญ์ บูรณะเศรณี")

def exit() :
    confirm = tkinter.messagebox.askquestion("Confirm","Are you sure to close it")
    if confirm == 'yes' :
        root.destroy()

myMenu = Menu()
root.config(menu=myMenu)
menuitem = Menu()
menuitem.add_command(label='How to use',command=clickedHowtouse)
menuitem.add_command(label='About Developer',command=clickedshowdeveloper)
menuitem.add_command(label='Exit',command=exit)
myMenu.add_cascade(label='About',menu=menuitem)

########Gender######

def selection() :
    value = radio.get()
    if value == 'Male' :
        gender = 'Male'
        print(gender)
    else :
        gender = 'Female'
        print(gender)

radio = StringVar()
R1=Radiobutton(leftframe,text='Male',variable=radio,value='Male',bg='white',command=selection).place(relx=0.4,rely=0.03) #รอเพิ่มcommand
gendertext = Label(leftframe,bg='white',text='Gender :',font=('Arial 13')).place(relx=0.1,rely=0.03)
R2=Radiobutton(leftframe,text='Female',variable=radio,value='Female',bg='white',command=selection).place(relx=0.6,rely=0.03)

#######Age##############
 
ageword = Label(leftframe,fg='black',bg='white',font=('Arial 13'),text = "Age :").place(relx=0.1,rely=0.2)#รอเพิ่มCommand
txtofage = IntVar()
textage = Entry(leftframe,width=10,fg='black',border=1,bg='white',font=('Arial 13'))
textyear = Label(leftframe,fg='black',bg='white',font=('Arial 13'),text = "Years").place(relx=0.7,rely=0.2)
textage.delete(0,'end')
textage.place(relx=0.4,rely=0.2)

####Weight####
     
weightword = Label(leftframe,fg='black',bg='white',font=('Arial 13'),text = "Weight :").place(relx=0.1,rely=0.4) #รอเพิ่มCommand
txtofweight = DoubleVar()
textweight = Entry(leftframe,width=10,fg='black',border=1,bg='white',font=('Arial 13'))
textweight.place(relx=0.4,rely=0.4)
textKilograms = Label(leftframe,fg='black',bg='white',font=('Arial 13'),text = "Kilograms").place(relx=0.7,rely=0.4)
textweight.delete(0,'end')

####Height####

heightword = Label(leftframe,text='Height :',bg='white',font=('Arial 13')).place(relx=0.1,rely=0.6) #รอเพิ่มCommand
txtofheight = DoubleVar()
textheight = Entry(leftframe,width=10,fg='black',border=1,bg='white',font=('Arial 13'))
textCentimeters = Label(leftframe,fg='black',bg='white',font=('Arial 13'),text = "Centimeters").place(relx=0.7,rely=0.6)
textheight.place(relx=0.4,rely=0.6)
textheight.delete(0,'end')

BMIlabel = Label(underleftframe,text='Bodymass and Bodyfat Index',fg = '#57a1f8',bg='white',font=('Microsoft Yahei UI Light',16,'bold')).place(relx=0.1,rely=0.02)

####SaveButton####

def caloriesin1day() :
    calories1day = Tk()
    calories1day.title("Smart Healthy Application")
    calories1day.geometry("825x400+600+200")
    calories1day.resizable(False,False)
    calories1day.config(bg='salmon')

    leftframeofcalories1day  = Frame(calories1day,width=350,height=290,bg='white')
    leftframeofcalories1day .place(x=50,y=50)

    rightframeofcalories1day  = Frame(calories1day,width=350,height=290,bg='white')
    rightframeofcalories1day .place(x=420,y=50)

    gender = radio.get()
    age = textage.get()
    weight = textweight.get()
    
    def calculate() :
        Diseasecal = choiceDisease .get()
        Activitycal = combo.get()
        print(gender,Diseasecal,Activitycal)
        
        
        def diabetes(weight) :
            precalories = 10 * float(weight) 
            score = [3,5,7]
            work = ['Low work','Medium work','Hard work']
            factorinput = Activitycal
            for e in work :
                if factorinput == e :
                    scoretotal = score[work.index(factorinput)]
            postcalories = precalories + (scoretotal * 100)
            return postcalories
    
    ##Calorie in take 2
        def BMRcal() :
            male = [(59.512 * float(weight)) - 30.4,(22.706 * float(weight)) + 504.3,(17.686 * float(weight)) + 658.3,(15.057 * float(weight)) + 692.2,(11.472 * float(weight)) + 873.1,(11.711 * float(weight)) + 587.7]
            female = [(58.317 * float(weight)) - 31.1 ,(20.315 * float(weight)) + 485.9,(13.384 * float(weight)) + 692.6,(14.818 * float(weight)) + 486.6,(8.126 * float(weight)) + 845.6,(9.082 * float(weight)) + 658.5]
            if gender == "male" or 'ชาย' :
                if float(age) < 3 :
                    bmr = male[0] 
                elif 3 <= float(age) <= 10 :
                    bmr = male[1]
                elif 11 <= float(age) <= 18 :
                    bmr = male[2]
                elif 19 <= float(age) <= 30 :
                    bmr = male[3]
                elif 31 <= float(age) <= 60 :
                    bmr = male[4]
                elif float(age) >= 61 :
                    bmr = male[5]
            elif gender == "female" or "หญิง" :
                if float(age) < 3 :
                    bmr = female[0] 
                elif 3 <= float(age) <= 10 :
                    bmr = female[1]
                elif 11 <= float(age) <= 18 :
                    bmr = female[2]
                elif 19 <= float(age) <= 30 :
                    bmr = female[3]
                elif 31 <= float(age) <= 60 :
                    bmr = female[4]
                elif float(age) >= 61 :
                    bmr = female[5]
            return bmr
   
        def suggestion(Diseasecal) :
            if Diseasecal == 'Diabetes' :
                Energy = diabetes(weight)
            else :
                bmr = BMRcal()
                factor = [1.4,1.7,2]
                workper = ["Low work","Medium work","Hard work"]
                work = Activitycal
                for e in workper :
                    if work == e :
                        Energy = bmr * factor[(workper.index(work))]
            return round(Energy,2)
    
        CaloriesResult = Label(rightframeofcalories1day,bg='white',text="In 1 day your calories are",font=('Microsoft Yahei UI Light',16)).place(relx=0.15,rely=0.35)
        CaloriesResult2 = Label(rightframeofcalories1day,bg='white',text=str(suggestion(Diseasecal))+ " Kilocalories",font=('Microsoft Yahei UI Light',16)).place(relx=0.22,rely=0.45)
        print(suggestion(Diseasecal))
    
    Head = Label(leftframeofcalories1day,text='Calories For 1 Day',fg = '#57a1f8',bg='white',font=('Microsoft Yahei UI Light',16,'bold')).place(relx=0.23,rely=0.02)

    TypeofDisease = Label(leftframeofcalories1day,fg='black',bg='white',text='Choose your disease :',font=('Microsoft Yahei UI Light',13)).place(relx=0.05,rely=0.2)
    choiceDisease = StringVar(value='Disease')
    comboDisease = ttk.Combobox(leftframeofcalories1day,textvariable=choiceDisease,width=12,font=('Microsoft Yahei UI Light',13))
    comboDisease['values'] = ("Diabetes",'Obese','None')
    comboDisease.place(relx=0.6,rely=0.2)

    Typeofrice = Label(leftframeofcalories1day,fg='black',bg='white',text='Choose the activity :',font=('Microsoft Yahei UI Light',13)).place(relx=0.05,rely=0.4)
    choice = StringVar(value='Activity')
    combo = ttk.Combobox(leftframeofcalories1day,textvariable=choice,width=12,font=('Microsoft Yahei UI Light',13))
    combo['values'] = ("Low work","Medium work","Hard work")
    combo.place(relx=0.6,rely=0.4)

    CalculateButton = Button(leftframeofcalories1day,text='Calculate',width=15,command=calculate).place(relx=0.35,rely=0.6)
    headResult = Label(rightframeofcalories1day,text='Result',fg = '#57a1f8',bg='white',font=('Microsoft Yahei UI Light',16,'bold')).place(relx=0.4,rely=0.02)

    calories1day.mainloop()

def firststep() :
    gender = radio.get()
    age = textage.get()
    weight = textweight.get()
    height = textheight.get()
    print(gender,age,weight,height)

    bmi = float(weight) / (float(height) / 100)**2 #### รอแก้
    if bmi < 18.5 :
        Totalofbmi = "Your BMI is underweight range"
        print('You need to eat more')
    elif 18.5 < bmi < 24.9 :
        Totalofbmi = "Your BMI is healthy Weight range"
    elif 25.0 < bmi < 29.9 :
        Totalofbmi = "Your BMI is overweight range"
    elif bmi > 30 :
        Totalofbmi = "Your BMI is obese range"
    
    
    if gender == 'male' or 'ชาย' :
        if 1 <= float(age) <= 12 :
            bfp = (1.51 * bmi) - (0.70 * float(age)) - 2.2    
        elif float(age) > 12 :
            bfp = (1.20 * bmi) + (0.23 * float(age)) - 16.2
    elif gender  == 'female' or 'หญิง' :
        if 1 <= float(age) <= 12 :
            bfp = (1.51 * bmi) - (0.70 * float(age)) + 1.4 
        elif float(age) > 12 :
            bfp = (1.20 * bmi) + (0.23 * float(age)) - 5.4
    else : bfp = 0

    def criteriaofbfp(bfp):
        if gender == 'male' or 'ชาย' :
            if 2 <= bfp < 6 :
                Description = 'You are Essential fat'
            elif 6 <= bfp < 14 :
                Description = 'You are Athletes'
            elif 14 <= bfp < 18 :
                Description = 'You are Fitness'
            elif 18 <= bfp < 24 :
                Description = 'You are Fitness'
            else : Description = 'You are Obese'
        return Description
    Bmitext = Label(underleftframe,bg='white',text = Totalofbmi,font=('Microsoft Yahei UI Light',16)).place(relx=0.1,rely=0.3)
    BFPtext = Label(underleftframe,bg='white',text = criteriaofbfp(bfp),font=('Microsoft Yahei UI Light',16)).place(relx=0.1,rely=0.5)

savebutton = Button(leftframe,text='Calculator',width=10,command = firststep).place(relx=0.4,rely=0.8)    



#### Function ####
def get_incaloriesperladle() :
    caloriesperladle = Tk()
    caloriesperladle.title("Smart Healthy Application")
    caloriesperladle.geometry("825x400+600+200")
    caloriesperladle.resizable(False,False)
    caloriesperladle.config(bg='salmon')



##################################################################

    def save() :
        amount_of_rice = amountofriceEntry.get()
        type_of_rice = combo.get()
        Type_of_rice_and_kilocalories = {'brown rice':70,'rice berry':80,'white rice':80,'sticky rice':160,'japanese rice':118,'jasmine rice':80}
        kilocalories = Type_of_rice_and_kilocalories[type_of_rice.lower()] * int(amount_of_rice)
        print(amount_of_rice)
        print(type_of_rice)
        print(kilocalories)
        Result = Label(rightframe,bg='white',text = "You choose a " + str(type_of_rice) +  ' in ' + str(amount_of_rice) + ' scoops',font = ('Microsoft Yahei UI Light',16) ).place(relx=0.0,rely=0.3)
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

Headfunction = Label(rightframe,text='Function',fg = '#57a1f8',bg='white',font=('Microsoft Yahei UI Light',16,'bold')).place(relx=0.38,rely=0.02)
functionbutton1 = Button(rightframe,text='Calorie per ladle',bg = 'lightblue',font=('Microsoft Yahei UI Light',11),command=get_incaloriesperladle).place(relx=0.1,rely=0.3,width=140,height=40) 
functionbutton2 = Button(rightframe,text='Calorie for 1 days',bg = 'lightblue',font=('Microsoft Yahei UI Light',11),command=caloriesin1day).place(relx=0.55,rely=0.3,width=140,height=40) #รอเพิ่มCommand

HeadAdvise= Label(underrightframe,text='Advise',fg = '#57a1f8',bg='white',font=('Microsoft Yahei UI Light',16,'bold')).place(relx=0.4,rely=0.02)

def webscrape() :
    window = Tk()
    window.title('Calories')
    text_box = ttk.Text(window)
    text_box.pack()
### Nutrition ####
    file_path = "Food.txt"  # กำหนดชื่อไฟล์ที่ต้องการเปิด
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()
        text_box.delete(1.0, ttk.END)  # ล้างข้อความที่อยู่ใน Text widget
        text_box.insert(ttk.END, content)
    window.mainloop()
    

def on_enter(e) :
    textAdvise.delete(0,'end')
    
def on_leave(e) :
    name = textAdvise.get()
    if name == '' :
         textAdvise.insert(0,'Menu') 
        
textAdvise= Entry(underrightframe,width=35,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
textAdvise.place(relx=0.15,rely=0.2)
textAdvise.insert(0,'Menu')
textAdvise.bind('<FocusIn>',on_enter)
textAdvise.bind('<FocusOut>',on_leave)
Frame(underrightframe,width=295,height=2,bg='black').place(relx=0.15,rely=0.32)

webscrape = Button(underrightframe,text='Menu calories',font=('Microsoft Yahei UI Light',11),command=webscrape).place(relx=0.35,rely=0.35,width=140,height=40)


def on_enterofAdvise(e) :
    textAdviseResult.delete(0,'end')
    
def on_leaveofAdvise(e) :
    name = textAdviseResult.get()
    if name == '' :
         textAdviseResult.insert(0,'Exercise') 

def apiexercise() :
    activity = textAdviseResult.get()
    api_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(activity)
    response = requests.get(api_url, headers={'X-Api-Key': '/nj5rHE+RtwdIlzmHgDitA==25nG7trAOneV3LZy'})
    if response.status_code == requests.codes.ok:
        with open('calories_data.txt', 'w') as file:
            data = response.json()
            for item in data:
                file.write(str(item) + '\n')
            print('\n')
        print("Data saved successfully.")
    
    Exercisewindow = Tk()
    Exercisewindow.title('Calories')
    text_box = ttk.Text(Exercisewindow)
    text_box.pack()

    file_path = "calories_data.txt"  # กำหนดชื่อไฟล์ที่ต้องการเปิด
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()
        text_box.delete(1.0, ttk.END)  # ล้างข้อความที่อยู่ใน Text widget
        text_box.insert(ttk.END, content)
    Exercisewindow.mainloop()

    
textAdviseResult = Entry(underrightframe,width=35,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
textAdviseResult.place(relx=0.15,rely=0.6)
textAdviseResult.insert(0,'Exercise')
textAdviseResult.bind('<FocusIn>',on_enterofAdvise)
textAdviseResult.bind('<FocusOut>',on_leaveofAdvise)
Frame(underrightframe,width=295,height=2,bg='black').place(relx=0.15,rely=0.72)

Exercisebutton = Button(underrightframe,text='Exercise burned',font=('Microsoft Yahei UI Light',11),command=apiexercise).place(relx=0.35,rely=0.75,width=140,height=40)

root.mainloop()