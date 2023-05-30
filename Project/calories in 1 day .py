from tkinter import *
from tkinter import ttk

### เพศ กิจกรรม โรค

calories1day = Tk()
calories1day.title("Smart Healthy Application")
calories1day.geometry("825x400+600+200")
calories1day.resizable(False,False)
calories1day.config(bg='salmon')

leftframeofcalories1day = Frame(calories1day,width=350,height=290,bg='white')
leftframeofcalories1day.place(x=50,y=50)

rightframeofcalories1day = Frame(calories1day,width=350,height=290,bg='white')
rightframeofcalories1day.place(x=420,y=50)

gender = "male"
weight = 70
age = 10

def calculate() :
    Diseasecal = choiceDisease .get()
    Activitycal = combo.get()
    print(gender,Diseasecal,Activitycal)

    def diabetes(weight) :
        precalories = 10 * weight 
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
        male = [(59.512 * weight) - 30.4,(22.706 * weight) + 504.3,(17.686 * weight) + 658.3,(15.057 * weight) + 692.2,(11.472 * weight) + 873.1,(11.711 * weight) + 587.7]
        female = [(58.317 * weight) - 31.1 ,(20.315 * weight) + 485.9,(13.384 * weight) + 692.6,(14.818 * weight) + 486.6,(8.126 * weight) + 845.6,(9.082 * weight) + 658.5]
        if gender == "male" or 'ชาย' :
            if age < 3 :
                bmr = male[0] 
            elif 3 <= age <= 10 :
                bmr = male[1]
            elif 11 <= age <= 18 :
                bmr = male[2]
            elif 19 <= age <= 30 :
                bmr = male[3]
            elif 31 <= age <= 60 :
                bmr = male[4]
            elif age >= 61 :
                bmr = male[5]
        elif gender == "female" or "หญิง" :
            if age < 3 :
                bmr = female[0] 
            elif 3 <= age <= 10 :
                bmr = female[1]
            elif 11 <= age <= 18 :
                bmr = female[2]
            elif 19 <= age <= 30 :
                bmr = female[3]
            elif 31 <= age <= 60 :
                bmr = female[4]
            elif age >= 61 :
                bmr = female[5]
        else :
            bmr = 'Error'
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