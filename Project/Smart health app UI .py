from tkinter import *
import tkinter.messagebox


root = Tk()
root.title("Smart Healthy Application")


#Resolution
root.geometry("925x500+300+200") #res
Welcome = Label(root,text="Welcome to smart healthy application",font=('Microsoft Yahei UI Light',16,'bold')).place(x=0,y=0)
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


#Gender
Genderword = Label(root,width=25,fg='black',font=('Microsoft Yahei UI Light',11,'bold'),text = "Input your gender :").pack() #รอเพิ่มCommand
genderoptions = ['Male','Female']
Genderclicked = StringVar()
Genderclicked.set(genderoptions[0])
Genderdropdown = OptionMenu(root,Genderclicked, *genderoptions).pack()

#Age Input

def on_enter(e) :
    textage.delete(0,'end')
    
def on_leave(e) :
    name = textage.get()
    if name == '' :
        textage.insert(0,'กรุณาใส่เป็นตัวเลข') 
        
ageword = Label(root,width=25,fg='black',font=('Microsoft Yahei UI Light',11,'bold'),text = "Input your age :").pack() #รอเพิ่มCommand
txtofage = IntVar()
textage = Entry(root,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
textage.delete(0,'end')
textage.insert(0,'กรุณาใส่เป็นตัวเลข')
textage.pack()
textage.bind('<FocusIn>',on_enter)
textage.bind('<FocusOut>',on_leave)

#Weight input

def on_enter(e) :
    textweight.delete(0,'end')
    
def on_leave(e) :
    name = textweight.get()
    if name == '' :
        textweight.insert(0,'กรุณาใส่เป็นตัวเลข') 
        
weightword = Label(root,width=25,fg='black',font=('Microsoft Yahei UI Light',11,'bold'),text = "Input your weight in kilograms :").pack() #รอเพิ่มCommand
txtofweight = DoubleVar()
textweight = Entry(root,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
textweight.pack()
textweight.delete(0,'end')
textweight.insert(0,'กรุณาใส่เป็นตัวเลข')
textweight.bind('<FocusIn>',on_enter)
textweight.bind('<FocusOut>',on_leave)

#Height input
heightword = Label(root,text='Input your height in centimeters :').pack() #รอเพิ่มCommand
txtofheight = DoubleVar()
textheight = Entry(root,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
textheight.pack()
textweight.bind('<FocusIn>',on_enter)
textweight.bind('<FocusOut>',on_leave)

def firststep() :
    gender = Genderclicked.get()
    age = txtofage.get()
    weight = txtofweight.get()
    height = txtofheight.get()
    print(gender,age,weight,height)

        
savebutton = Button(root,text='Save',command = firststep).place(x=350,y=210,width=70,height=25) #รอเพิ่มCommand


## functionbutton
functionbutton1 = Button(root,text='Calorie per ladle',).place(x=90,y=250,width=150,height=40) #รอเพิ่มCommand
functionbutton2 = Button(root,text='Calorie in 1 days',).place(x=350,y=250,width=150,height=40) #รอเพิ่มCommand
functionbutton3 = Button(root,text='Calculate your BMI',).place(x=90,y=340,width=150,height=40) #รอเพิ่มCommand
functionbutton4 = Button(root,text='Bodymass Index',).place(x=350,y=340,width=150,height=40) #รอเพิ่มCommand

root.mainloop()
