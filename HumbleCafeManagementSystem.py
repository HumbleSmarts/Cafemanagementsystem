from datetime import date
from tkinter import*
import tkinter
import tkinter.ttk
import tkinter.messagebox as messagebox
import random
import time
import datetime

from tkinter import *

from random import triangular

"""def register_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info+".txt", "w")
    file.write(username_info)
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Successful", fg = "green",
          font = ("calibri", 11)).pack()
    
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter detail below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack() 
    Button(screen1, text = "Already have am account?", command = login).pack()

def login_user():
    user = input("Username: ")
    passw = input("Password: ")
    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (user in us) and (passw in pw):
            print ("login successful!")
            return True

    print ("Wrong username / password")
    return False

def menu():
    HumbleCafeManagementSystem.py
    #here's a menu that the user can access if he logged in.

def main():
    login_user()
    log = login
    if log == True:
        menu()"""
        


"""def login_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info+".txt", "r")
    file.read(None)
    file.read(None)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(screen1, text = "Login Successful", fg = "green", font = ("calibri", 11)).pack()
    print("Login session started")
    file=open (HumbleCafeManagementSystem.py , "r")
    file.read(None)
    file.read(None)
    file.close()


def HumbleCafeManagementSystem():
    HumbleCafeManagementSystem.py = HumbleCafeManagementSystem.get()

    file=open (HumbleCafeManagementSystem+".py", "r", "w")
    file.read(None)
    file.read(None)
    file.close()

    
def login():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Login")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter detail below...").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Login", width = 10, height = 1, command = login_user).pack()
    Label(screen1, text = "Forget you password?").pack()
    Button(screen1, text = "Don't have am account?", command = register).pack()

    

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Registration form")
    Label(text = "Login Details", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()

    screen.mainloop()

main_screen()"""



"""start_date = datetime.date.today()
print(start_date)"""


root = tkinter.Tk()
root.geometry("1280x800+0+0")
root.title("Humble Cafe Management System")
root.configure(background='black')

Tops = Frame(root, width= 1280, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width= 600, height=550, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width= 340, height=450, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a= Frame(f1, width= 800, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a= Frame(f1, width= 800, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2= Frame(f2, width= 340, height=350, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2= Frame(f2, width= 340, height=200, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa= Frame(f1a, width= 300, height=230, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab= Frame(f1a, width= 300, height=230, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa= Frame(f2a, width= 350, height=230, bd=14, relief="raise")
f2aa.pack(side=LEFT)

f2ab= Frame(f2a, width= 350, height=230, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')


#===========================CostofItem=================================================
def CostofItem():
    Item1=float(E_Latta.get())
    Item2=float(E_Espresso.get())
    Item3=float(E_Iced_Latta.get())
    Item4=float(E_Vale_Coffee.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_African_Coffee.get())
    Item7=float(E_American_Coffee.get())
    Item8=float(E_Iced_Cappuccino.get())

    Item9=float(E_Coffee_Cake.get())
    Item10=float(E_Red_Velvet_Cake.get())
    Item11=float(E_Black_Forest_Cake.get())
    Item12=float(E_Boston_Cream_Cake.get())
    Item13=float(E_Lagos_Chocolate_Cake.get())
    Item14=float(E_Kilburn_Chocolate_Cake.get())
    Item15=float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16=float(E_Queen_Park_Chocolate_Cake.get())
    
    PriceofDrinks =(Item1 * 1.2) + (Item2 * 1.99) +(Item3 * 2.05) \
                            + (Item4 * 1.89) + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)

    PriceofCakes =(Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99) \
                            + (Item12 * 1.49) + (Item13 * 1.8) + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 * 1.99)

    DrinksPrice ="#", str('%.2f'%(PriceofDrinks))
    CakesPrice ="#", str('%.2f'%(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    ServiceCharge = 1.59

    SubTotalofITEMS ='#', str('%.2f'%(PriceofDrinks + PriceofCakes ))
    SubTotal.set(SubTotalofITEMS)

    Tax ="#", str('%.2f'%((PriceofDrinks + PriceofCakes ) * 0.15))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes) * 0.15)
    TC ="#", str('%.2f'%(PriceofDrinks + PriceofCakes  + TT))
    TotalCost.set(TC)
    


def dExit():
    dExit = messagebox.askyesno("Quit System", "Do you want to quit")
    if dExit:
        root.destroy()
        return

def ePrint():
    ePrint = massagebox.askyesno(" Print System ", " Do you what to print ")
    if ePrint:
        root.exit()
        return


def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)


    E_Latta.set("0")
    E_Espresso.set("0")
    E_Iced_Latta.set("0")
    E_Vale_Coffee.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")


    E_Coffee_Cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")


    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

    txtLatta.configure(state= DISABLED)
    txtEspresso.configure(state= DISABLED)
    txtIced_Latta.configure(state= DISABLED)
    txtVale_Coffee.configure(state= DISABLED)
    txtCappuccino.configure(state= DISABLED)
    txtAfrican_Coffee.configure(state= DISABLED)
    txtAmerican_Coffee.configure(state= DISABLED)
    txtIced_Cappuccino.configure(state= DISABLED)
    txtCoffee_Cake.configure(state= DISABLED)
    txtRed_Velvet_Cake.configure(state= DISABLED)
    txtBlack_Forest_Cake.configure(state= DISABLED)
    txtBoston_Cream_Cake.configure(state= DISABLED)
    txtLagos_Chocolate_Cake.configure(state= DISABLED)
    txtKilburn_Chocolate_Cake.configure(state= DISABLED)
    txtCarlton_Hill_Chocolate_Cake.configure(state= DISABLED)
    txtQueen_Park_Chocolate_Cake.configure(state= DISABLED)
    
def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10987, 599879)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t\t' + DateOfOrder.get() +"\n")
    txtReceipt.insert(END,'Items\t\t\t\t\t' + "Cost of Items \n\n")
    txtReceipt.insert(END,'Latta: \t\t\t\t\t' + E_Latta.get()+ "\n")
    txtReceipt.insert(END,'Espresso: \t\t\t\t\t' + E_Espresso.get()+"\n")
    txtReceipt.insert(END, 'Iced Latta: \t\t\t\t\t' + E_Iced_Latta.get()+"\n")
    txtReceipt.insert(END, 'Vale Coffee: \t\t\t\t\t' + E_Vale_Coffee.get()+"\n")
    txtReceipt.insert(END, 'Cappuccino: \t\t\t\t\t' + E_Cappuccino.get() +"\n")
    txtReceipt.insert(END, 'African Coffee: \t\t\t\t\t' + E_African_Coffee.get()+ "\n")
    txtReceipt.insert(END, 'American Coffee: \t\t\t\t\t' + E_American_Coffee.get()+ "\n")
    txtReceipt.insert(END, 'Iced Cappuccino: \t\t\t\t\t' + E_Iced_Cappuccino.get() + "\n")
    txtReceipt.insert(END, 'Coffee Cake: \t\t\t\t\t' + E_Coffee_Cake.get() +"\n")
    txtReceipt.insert(END, 'Red Velvet Cake: \t\t\t\t\t' + E_Red_Velvet_Cake.get() +"\n")
    txtReceipt.insert(END, 'Black Forest Cake: \t\t\t\t\t' + E_Black_Forest_Cake.get() + "\n")
    txtReceipt.insert(END, 'Boston Cream Cake: \t\t\t\t\t' + E_Boston_Cream_Cake.get() + "\n")
    txtReceipt.insert(END, 'Lagos Chocolate Cake: \t\t\t\t\t' + E_Lagos_Chocolate_Cake.get() +"\n")
    txtReceipt.insert(END, 'Kilburn Chocolate Cake: \t\t\t\t\t' + E_Kilburn_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Carlton Hill Chocolate Cake: \t\t\t\t\t' + E_Carlton_Hill_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Queens Park Chocolate Cake: \t\t\t\t\t' + E_Queen_Park_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Cost of Drinks: \t\t' + CostofDrinks.get() + '\tTax Paid:\t\t' +PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Cost of Cakes: \t\t' + CostofCakes.get() + '\tSubTotal:\t\t' +SubTotal.get()+"\n")
    txtReceipt.insert(END, 'Service Charge: \t\t' + ServiceCharge.get() + '\tTotal Cost:\t\t' +TotalCost.get()+"\n")
    
    
#=============================Heading======================================
lblInfo = Label(Tops, font=('arial', 75, 'bold'), text="Humble Cafe Management System",
                bd=8, anchor='w')
lblInfo.grid(row=0,column=0)

#================================Calculator===============================

def chkbutton_value():
    if (var1.get() == 1):
        txtLatta.configure(state= NORMAL)
    elif var1.get()== 0:
        txtLatta.configure(state= DISABLED)
        E_Latta.set("0")
    if (var2.get() == 1):
        txtEspresso.configure(state= NORMAL)
    elif var2.get()== 0:
        txtEspresso.configure(state= DISABLED)
        E_Espresso.set("0")
    if (var3.get() == 1):
        txtIced_Latta.configure(state= NORMAL)
    elif var3.get()== 0:
        txtIced_Latta.configure(state= DISABLED)
        E_Iced_Latta.set("0")
    if (var4.get() == 1):
        txtVale_Coffee.configure(state= NORMAL)
    elif var4.get()== 0:
        txtVale_Coffee.configure(state= DISABLED)
        E_Vale_Coffee.set("0")
    if (var5.get() == 1):
        txtCappuccino.configure(state= NORMAL)
    elif var5.get()== 0:
        txtCappuccino.configure(state= DISABLED)
        E_Cappuccino.set("0")
    if (var6.get() == 1):
        txtAfrican_Coffee.configure(state= NORMAL)
    elif var6.get()== 0:
        txtAfrican_Coffee.configure(state= DISABLED)
        E_African_Coffee.set("0")
    if (var7.get() == 1):
        txtAmerican_Coffee.configure(state= NORMAL)
    elif var7.get()== 0:
        txtAmerican_Coffee.configure(state= DISABLED)
        E_American_Coffee.set("0")
    if (var8.get() == 1):
        txtIced_Cappuccino.configure(state= NORMAL)
    elif var8.get()== 0:
        txtIced_Cappuccino.configure(state= DISABLED)
        E_Iced_Cappuccino.set("0")
    if (var9.get() == 1):
        txtCoffee_Cake.configure(state= NORMAL)
    elif var9.get()== 0:
        txtCoffee_Cake.configure(state= DISABLED)
        E_Coffee_Cake.set("0")
    if (var10.get() == 1):
        txtRed_Velvet_Cake.configure(state= NORMAL)
    elif var10.get()== 0:
        txtRed_Velvet_Cake.configure(state= DISABLED)
        E_Red_Velvet_Cake.set("0")
    if (var11.get() == 1):
        txtBlack_Forest_Cake.configure(state= NORMAL)
    elif var11.get()== 0:
        txtBlack_Forest_Cake.configure(state= DISABLED)
        E_Black_Forest_Cake.set("0")
    if (var12.get() == 1):
        txtBoston_Cream_Cake.configure(state= NORMAL)
    elif var12.get()== 0:
        txtBoston_Cream_Cake.configure(state= DISABLED)
        E_Boston_Cream_Cake.set("0")
    if (var13.get() == 1):
        txtLagos_Chocolate_Cake.configure(state= NORMAL)
    elif var13.get()== 0:
        txtLagos_Chocolate_Cake.configure(state= DISABLED)
        E_Lagos_Chocolate_Cake.set("0")
    if (var14.get() == 1):
        txtKilburn_Chocolate_Cake.configure(state= NORMAL)
    elif var14.get()== 0:
        txtKilburn_Chocolate_Cake.configure(state= DISABLED)
        E_Kilburn_Chocolate_Cake.set("0")
    if (var15.get() == 1):
        txtCarlton_Hill_Chocolate_Cake.configure(state= NORMAL)
    elif var15.get()== 0:
        txtCarlton_Hill_Chocolate_Cake.configure(state= DISABLED)
        E_Carlton_Hill_Chocolate_Cake.set("0")
    if (var16.get() == 1):
        txtQueen_Park_Chocolate_Cake.configure(state= NORMAL)
    elif var16.get()== 0:
        txtQueen_Park_Chocolate_Cake.configure(state= DISABLED)
        E_Queen_Park_Chocolate_Cake.set("0")



#===========================variables============================================
var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()

DateOfOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofCakes=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()

E_Latta=StringVar()
E_Espresso=StringVar()
E_Iced_Latta=StringVar()
E_Vale_Coffee=StringVar()
E_Cappuccino=StringVar()
E_African_Coffee=StringVar()
E_American_Coffee=StringVar()
E_Iced_Cappuccino=StringVar()


E_Coffee_Cake=StringVar()
E_Red_Velvet_Cake=StringVar()
E_Black_Forest_Cake=StringVar()
E_Boston_Cream_Cake=StringVar()
E_Lagos_Chocolate_Cake=StringVar()
E_Kilburn_Chocolate_Cake=StringVar()
E_Carlton_Hill_Chocolate_Cake=StringVar()
E_Queen_Park_Chocolate_Cake=StringVar()


E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latta.set("0")
E_Vale_Coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")


E_Coffee_Cake.set("0")
E_Red_Velvet_Cake.set("0")
E_Black_Forest_Cake.set("0")
E_Boston_Cream_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Carlton_Hill_Chocolate_Cake.set("0")
E_Queen_Park_Chocolate_Cake.set("0")


DateOfOrder.set(time.strftime("%d /%m /%y :: %H: %M: %S"))




#============================Drinks======================================================
Latta = Checkbutton(f1aa, text="Latta \t", variable = var1, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 0, sticky=W)
Espresso = Checkbutton(f1aa, text="Espresso \t", variable = var2, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 1, sticky=W)
Iced_Latta = Checkbutton(f1aa, text="Iced_Latta \t", variable = var3, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 2, sticky=W)
Vale_Coffee = Checkbutton(f1aa, text="Vale_Coffee \t", variable = var4, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 3, sticky=W)
Cappuccino = Checkbutton(f1aa, text="Cappuccino \t", variable = var5, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 4, sticky=W)
African_Coffee = Checkbutton(f1aa, text="African_Coffee \t", variable = var6, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 5, sticky=W)
American_Coffee = Checkbutton(f1aa, text="American_Coffee \t", variable = var7, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 6, sticky=W)
Iced_Cappuccino = Checkbutton(f1aa, text="Iced_Cappuccino \t", variable = var8, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 7, sticky=W)

#============================Cakes======================================================
CoffeeCake = Checkbutton(f1ab, text="Coffee Cake \t", variable = var9, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 0, sticky=W)
Red_Velvet_Cake = Checkbutton(f1ab, text="Red Velvet Cake \t", variable = var10, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 1, sticky=W)
Black_Forest_Cake = Checkbutton(f1ab, text="Black Forest Cake \t", variable = var11, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 2, sticky=W)
Boston_Cream_Cake = Checkbutton(f1ab, text="Boston Cream Cake \t", variable = var12, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 3, sticky=W)
Lagos_Chocolate_Cake = Checkbutton(f1ab, text="Lagos Chocolate Cake \t", variable = var13, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 4, sticky=W)
Kilburn_Chocolate_Cake = Checkbutton(f1ab, text="Kilburn Chocolate Cake \t", variable = var14, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 5, sticky=W)
Carlton_Hill_Chocolate_Cake = Checkbutton(f1ab, text="Carlton Hill Chocolate Cake \t", variable = var15, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 6, sticky=W)
Queen_Park_Chocolate_Cake = Checkbutton(f1ab, text="Queen Park Chocolate Cake \t", variable = var16, onvalue = 1, offvalue=0,
                    font=('arial', 17, 'bold'), command=chkbutton_value).grid(row = 7, sticky=W)

#============================Enter Widget For Drinks============================================
txtLatta = Entry(f1aa,font=('arial', 17, 'bold'), bd=8, width=6,
                 justify='left', textvariable=E_Latta, state= DISABLED)
txtLatta.grid(row =0, column=1)                 
txtEspresso = Entry(f1aa,font=('arial', 17, 'bold'), bd=8, width=6,
           justify='left', textvariable=E_Espresso, state= DISABLED)
txtEspresso.grid(row =1, column=1)                 
txtIced_Latta = Entry(f1aa,font=('arial', 17, 'bold'), bd=8, width=6,
           justify='left', textvariable=E_Iced_Latta, state= DISABLED)
txtIced_Latta.grid(row =2, column=1)                 
txtVale_Coffee = Entry(f1aa,font=('arial', 17, 'bold'), bd=8, width=6,
           justify='left', textvariable=E_Vale_Coffee, state= DISABLED)
txtVale_Coffee.grid(row =3, column=1)                 
txtCappuccino = Entry(f1aa,font=('arial', 17, 'bold'), bd=8, width=6,
          justify='left', textvariable=E_Cappuccino, state= DISABLED)
txtCappuccino.grid(row =4, column=1)                 
txtAfrican_Coffee = Entry(f1aa,font=('arial', 17, 'bold'), bd=8, width=6,
        justify='left', textvariable=E_African_Coffee, state= DISABLED)
txtAfrican_Coffee.grid(row =5, column=1)                 
txtAmerican_Coffee = Entry(f1aa,font=('arial', 17, 'bold'), bd=8, width=6,
                           justify='left', textvariable=E_American_Coffee, state= DISABLED)
txtAmerican_Coffee.grid(row =6, column=1)                 
txtIced_Cappuccino = Entry(f1aa,font=('arial', 17, 'bold'), bd=8, width=6,
                           justify='left', textvariable=E_Iced_Cappuccino, state= DISABLED)
txtIced_Cappuccino.grid(row =7, column=1)                 



#============================Enter Widget For Cakes============================================
txtCoffee_Cake = Entry(f1ab,font=('arial', 16, 'bold'), bd=8, width=6,
                       justify='left', textvariable=E_Coffee_Cake, state= DISABLED)
txtCoffee_Cake.grid(row =0, column=1)
txtRed_Velvet_Cake = Entry(f1ab,font=('arial', 16, 'bold'), bd=8, width=6,
                           justify='left', textvariable=E_Red_Velvet_Cake, state= DISABLED)
txtRed_Velvet_Cake.grid(row =1, column=1)
txtBlack_Forest_Cake = Entry(f1ab,font=('arial', 16, 'bold'), bd=8, width=6,
                             justify='left', textvariable=E_Black_Forest_Cake, state= DISABLED)
txtBlack_Forest_Cake.grid(row =2, column=1)
txtBoston_Cream_Cake = Entry(f1ab,font=('arial', 16, 'bold'), bd=8, width=6,
                             justify='left', textvariable=E_Boston_Cream_Cake, state= DISABLED)
txtBoston_Cream_Cake.grid(row =3, column=1)
txtLagos_Chocolate_Cake = Entry(f1ab,font=('arial', 16, 'bold'), bd=8,
                     width=6, justify='left', textvariable=E_Lagos_Chocolate_Cake, state= DISABLED)
txtLagos_Chocolate_Cake.grid(row =4, column=1)
txtKilburn_Chocolate_Cake = Entry(f1ab,font=('arial', 16, 'bold'), bd=8,
                  width=6, justify='left', textvariable=E_Kilburn_Chocolate_Cake, state= DISABLED)
txtKilburn_Chocolate_Cake.grid(row =5, column=1)
txtCarlton_Hill_Chocolate_Cake = Entry(f1ab,font=('arial', 16, 'bold'),
         bd=8, width=6, justify='left', textvariable=E_Carlton_Hill_Chocolate_Cake, state= DISABLED)
txtCarlton_Hill_Chocolate_Cake.grid(row =6, column=1)
txtQueen_Park_Chocolate_Cake = Entry(f1ab,font=('arial', 16, 'bold'),
      bd=8, width=6, justify='left', textvariable=E_Queen_Park_Chocolate_Cake, state= DISABLED)
txtQueen_Park_Chocolate_Cake.grid(row =7, column=1)


#===================================Cost of items information========================================
lblCostofDrinks=Label(f2aa, font=('arial', 16, 'bold'),
                      text="Cost of Drinks", bd=8, anchor='w')
lblCostofDrinks.grid(row = 2, column =0, sticky=W)

txtCostofDrinks=Entry(f2aa, font=('arial', 16, 'bold'),bd=8,
              insertwidth=2,justify = 'left',textvariable=CostofDrinks)
txtCostofDrinks.grid(row = 2, column=1)

lblCostofCakes=Label(f2aa, font=('arial', 16, 'bold'),
                     text="Cost of Cakes", bd=8, anchor='w')
lblCostofCakes.grid(row = 3, column =0, sticky=W)

txtCostofCakes=Entry(f2aa, font=('arial', 16, 'bold'),bd=8, insertwidth=2,
                     justify = 'left',textvariable= CostofCakes)
txtCostofCakes.grid(row = 3, column=1)

lblServiceChange=Label(f2aa, font=('arial', 16, 'bold'),
                       text="Service Change", bd=8, anchor='w')
lblServiceChange.grid(row = 4, column =0, sticky=W)

txtServiceChange=Entry(f2aa, font=('arial', 16, 'bold'),bd=8, insertwidth=2,
                       justify = 'left', textvariable=ServiceCharge)
txtServiceChange.grid(row = 4, column=1)

    
#===================================Payment Information========================================
lblPaidTax=Label(f2ab, font=('arial', 16, 'bold'), text="Paid Tax", bd=8)
lblPaidTax.grid(row = 2, column =0, sticky=W)
txtPaidTax=Entry(f2ab, font=('arial', 16, 'bold'),bd=8, insertwidth=2,
                 justify = 'left', textvariable=PaidTax)
txtPaidTax.grid(row = 2, column=1)

lblSubTotal=Label(f2ab, font=('arial', 16, 'bold'), text="Sub Total", bd=8)
lblSubTotal.grid(row = 3, column =0, sticky=W)
txtSubTotal=Entry(f2ab, font=('arial', 16, 'bold'),bd=8, insertwidth=2,
                  justify = 'left', textvariable=SubTotal)
txtSubTotal.grid(row = 3, column=1)

lblTotalCost=Label(f2ab, font=('arial', 16, 'bold'), text="Total Cost", bd=8)
lblTotalCost.grid(row = 4, column =0, sticky=W)
txtTotalCost=Entry(f2ab, font=('arial', 16, 'bold'),bd=8, insertwidth=2,
                   justify = 'left',textvariable=TotalCost)
txtTotalCost.grid(row = 4, column=1)



#============================Information/Receipt===================================================
lblReceipt = Label(ft2,font=('arial', 16,'bold'), text="Receipt", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0,sticky=W)
txtReceipt = Text(ft2,bd=8, width=70, height=36, bg="white",
                  font=('arial', 11, 'bold'))
txtReceipt.grid(row =1, column=0)

#================================ft2===============================================
lblReceipt = Label(ft2,font = ('arial', 16, 'bold'), text="Recipt:", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)#16
txtReceipt = Text(ft2, width = 70, height = 36, bg = "white", bd =8,
                  font=('arial', 11, 'bold'))
txtReceipt.grid(row = 1, column = 0)#20/09/19


#===================================Button===========================================
btnTotal=Button(fb2,padx=6,pady=1, bd=4, fg="black", font=('arial',14,'bold'),
           width=12,  text="Total", command = CostofItem).grid(row=0, column=0)

btnReceipt=Button(fb2,padx=6,pady=1, bd=4, fg="black", font=('arial',14,'bold'),
            width=10, text="Receipt", command = Receipt).grid(row=0, column=1)

btnReset=Button(fb2,padx=6,pady=1, bd=4, fg="black", font=('arial',14,'bold'),
             width=12, text="Reset", command = Reset).grid(row=0, column=2)

btnPrint=Button(fb2,padx=6,pady=1, bd=4, fg="black", font=('arial',14,'bold'),
             width=10, text="Print", command = ePrint).grid(row=0, column=3)

btnExit=Button(fb2,padx=6,pady=1, bd=4, fg="black", font=('arial',14,'bold'),
             width=10, text="Exit", command = dExit).grid(row=0, column=4)


# The exit buttom wasn't responding until I got to Infornatis Academy (JSIIT)
#Kazaure. i rewote the programming amd runed it and it started responding.
#17-10-2019 Humble Smarts


#    @Humble Wisdom Abraham

#btnReset=Button(fb2,padx=6,pady=1, bd=4, fg="black", font=('arial',14,'bold'),
 #            width=5, text="Reset", command = Reset).grid(row=0, column=2)

root.mainloop()
