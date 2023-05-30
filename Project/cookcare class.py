class User :
    def __init__(self) :
        self.sex = str(input("What is your gender? :")).lower()
        self.age = int(input("What is your age? :"))
        self.weight = int(input("What is your weight(kg)? :"))
        self.height = int(input("What is your height(cm)? :"))
    
    def calories_per_ladle() :
        amount_of_rice = int(input("What is your amount of rice per ladle? :")) 
        type_of_rice = input("What Type of your rice(Brownrice/)? :").lower()
        Type_of_rice_and_kilocalories = {'brown rice':70,'rice berry':80,'white rice':80,'sticky rice':160,'japanese rice':118,'jasmine rice':80}
        if 0 < amount_of_rice < 10 :
            kilocalories = Type_of_rice_and_kilocalories[type_of_rice.lower()] * int(amount_of_rice)
            return kilocalories
        
    def BMIcalandpredict(self) :
        bmi = self.weight / (self.height/100)**2
        Factor = False
        if bmi < 18.5 :
            Totalofbmi = "Your BMI is underweight range"
            Factor = True
            print('You need to eat more')
        elif  18.5 < bmi < 24.9 :
            Totalofbmi = "Your BMI is healthy Weight range"
            Factor = True
        elif 25.0 < bmi < 29.9 :
            Totalofbmi = "Your BMI is overweight range"
        elif bmi > 30 :
            Totalofbmi = "Your BMI is obese range"
        else :
            Totalofbmi = "Error"
        return Totalofbmi , Factor
    
    def diabetes(self) :
        precalories = 10 * self.weight 
        score = [3,5,7]
        work = ['light work','normal work','hard work']
        print("What is your activity all day(approximate) (light work / normal work / hard work) ")
        factorinput = input("Input your activity :")
        for e in work :
            if factorinput == e :
                scoretotal = score[work.index(factorinput)]
        postcalories = precalories + (scoretotal * 100)
        return postcalories

    def suggestion(self,Disease) :
        if Disease == 'diabetes' :
            Energy = self.diabetes()
        else :
            bmr = self.BMRcal()
            factor = [1.4,1.7,2]
            workper = ["low work","medium work","hard work"]
            work = input("What is your activities in 1 day (low work,medium work,hard work) : ")
            for e in workper :
                if work == e :
                    Energy = bmr * factor[(workper.index(work))]
        return Energy

    def BMRcal(self) :
        if len(str(self.age)) == 2 or 1 :
            male = [(59.512 * self.weight) - 30.4,(22.706 * self.weight) + 504.3,(17.686 * self.weight) + 658.3,(15.057 * self.weight) + 692.2,(11.472 * self.weight) + 873.1,(11.711 * self.weight) + 587.7]
            female = [(58.317 * self.weight) - 31.1 ,(20.315 * self.weight) + 485.9,(13.384 * self.weight) + 692.6,(14.818 * self.weight) + 486.6,(8.126 * self.weight) + 845.6,(9.082 * self.weight) + 658.5]
            if self.sex == "male" or 'ชาย' :
                if self.age < 3 :
                    bmr = male[0] 
                elif 3 <= self.age <= 10 :
                    bmr = male[1]
                elif 11 <= self.age <= 18 :
                    bmr = male[2]
                elif 19 <= self.age <= 30 :
                    bmr = male[3]
                elif 31 <= self.age <= 60 :
                    bmr = male[4]
                elif self.age >= 61 :
                    bmr = male[5]
            elif self.sex == "female" or "หญิง" :
                if self.age < 3 :
                    bmr = female[0] 
                elif 3 <= self.age <= 10 :
                    bmr = female[1]
                elif 11 <= self.age <= 18 :
                    bmr = female[2]
                elif 19 <= self.age <= 30 :
                    bmr = female[3]
                elif 31 <= self.age <= 60 :
                    bmr = female[4]
                elif self.age >= 61 :
                    bmr = female[5]
            else :
                bmr = 'Error'
            return bmr

    def Bodyfatprint(self) :
        Bodyfat = Bodyfat(self)
        criteria = ['Essential fat','Athletes','Fitness','Average','obese']
        if self.sex == 'male' or self.sex == 'ชาย' :
            if 0 < Bodyfat < 2 :
                advise = 'Lower Essential fat'
            elif 2 < Bodyfat < 5 :
                advise = criteria[0]
            elif 6 < Bodyfat < 13 :
                advise = criteria[1]
            elif 14 < Bodyfat < 17 :
                advise = criteria[2]
            elif 18 < Bodyfat < 24 :
                advise = criteria[3]
            elif Bodyfat > 25 :
                advise = criteria[4]
            else : advise = 'Error'
        elif self.sex == 'female' or self.sex == 'หญิง' :
            if 0 < Bodyfat < 10 : 
                advise = 'Lower Essemtial fat'
            elif 10 < Bodyfat < 13 :
                advise = criteria[0]
            elif 14 < Bodyfat < 20 :
                advise = criteria[1]
            elif 21 < Bodyfat < 24 :
                advise = criteria[2]
            elif 25 < Bodyfat < 31 :
                advise = criteria[3]
            elif Bodyfat > 32 :
                advise = criteria[4]
            else : advise = 'Error'
        else : advise = 'Error'
        return advise
        
    
    def Bodyfat(self) : # BMI METHOD
        bmi = self.weight / (self.height/100)**2
        if self.sex == 'male' or 'ชาย' :
            if 1 <= self.age <= 12 :
                bfp = (1.51 * bmi) - (0.70 * self.age) - 2.2    
            elif self.age > 12 :
                bfp = (1.20 * bmi) + (0.23 * self.age) - 16.2
        elif self.sex == 'female' or 'หญิง' :
            if 1 <= self.age <= 12 :
                bfp = (1.51 * bmi) - (0.70 * self.age) + 1.4 
            elif self.age > 12 :
                bfp = (1.20 * bmi) + (0.23 * self.age) - 5.4
        else : bfp = 0
        return round(bfp,2)

    


user = User()
print("-----What prediction did you prefer-----(Find calorie per ladle(1) / Calculate your BMI(2) / Calorie per day(3) / Body Fat(4))")
function_ = input('Function :') .lower()
print('---------------------------------------------')
if function_ == 'find calorie per ladle' or function_ == '1'  :
    print(user.calories_per_ladle())
elif function_ == 'calculate your bmi' or function_ == '2' :
    print(user.BMIcalandpredict()[0])
elif function_ == 'calorie per day' or function_ == '3':
    Disease = input("What is your disease(Obesity/Diabetes)? : ").lower()
    print(user.suggestion(Disease))



        
    



