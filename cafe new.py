# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 08:31:18 2022

@author: Administrator
"""

from tkinter import*
import random
import time;
import datetime


root= Tk()
root.title("Mocha Tree")
root.configure(background='#5F755E')
root.attributes('-fullscreen', True)

Tops = Frame(root, width=1350,height=100,bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900,height=750,bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width=440,height=750,bd=8, relief="raise")
f2.pack(side=RIGHT)

ft2 = Frame(f2, width=440,height=450,bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440,height=250,bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1a = Frame(f1, width=900,height=430,bd=8, relief="raise")
f1a.pack(side=TOP)
# f2a = Frame(f1, width=900,height=320,bd=6, relief="raise")
# f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width = 400, height=630,bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width = 400, height=630,bd=16, relief="raise")
f1ab.pack(side=RIGHT)


# f2aa = Frame(f2a, width = 450, height=330,bd=14, relief="raise")
# f2aa.pack(side=LEFT)
# f2ab = Frame(f2a, width = 450, height=330,bd=14, relief="raise")
# f2ab.pack(side=RIGHT)

Tops.configure(background='#5F755E')
f1.configure(background='#5F755E')
f2.configure(background='#5F755E')

#==================================================================HEADING==========================================================================

lblInfo = Label(Tops, font=('arial',60,'bold'), text= " Mocha Tree ", bd=10)
lblInfo.grid(row=0,column=0)

#===================================================================COST OF ITEMS=============================================================

def CostofItems():
    Item1=float(E_Latta.get())
    Item2=float(E_Coke.get())
    Item3=float(E_Iced_Latta.get())
    Item4=float(E_Coffee.get())
    Item5=float(E_Cappuccin.get())
    Item6=float(E_Tea.get()) 
    Item7=float(E_Cold_coffee.get())
    Item8=float(E_Beer.get())
    
    Item9=float(E_Coffee_cake.get()) 
    Item10=float(E_Black_forest.get())
    Item11=float(E_Cream_cake.get())
    Item12=float(E_Lagoos_cake.get())
    Item13=float(E_Fruit_cake.get())
    Item14=float(E_Chocolate_cake.get())
    Item15=float(E_Chocolava.get())
    Item16=float(E_Bread_cake.get())
    Item17 = float(E_Menu_Of_Day1.get())
    Item18 = float(E_Menu_Of_Day2.get())
    Item19 = float(E_Season_Special_1.get())
    Item20 = float(E_Season_Special_2.get())

    PriceofDrinks = (Item1 * 12) + (Item2 * 25.5) + (Item3 * 24.99) + (Item4 * 10.29) + (Item5 * 20.20) + (Item6 * 5.9) + (Item7 * 12.99) + (Item8 * 55.45) + (Item17 * 70) + (Item18 * 70) + (Item19 * 90) + (Item20 * 90)

    PriceofCakes = (Item9 * 12.2) + (Item10 * 15.99) + (Item11 * 40.99) + (Item12 * 22.29) + (Item13 * 25.20) + (Item14 * 30.9) + (Item15 * 35.99) + (Item16 * 40.45)

    DrinksPrice ="Rs", str ('%.2f'%(PriceofDrinks))

    CakesPrice ="Rs", str ('%.2f'%(PriceofCakes))

    CostofCakes.set(CakesPrice)

    CostofDrinks.set(DrinksPrice)

    SC= "Rs" , str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs" , str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax= "Rs" , str('%.2f'%((PriceofDrinks + PriceofCakes + 1.59)* 0.15))
    PaidTax.set(Tax)

    TT = ((PriceofDrinks + PriceofCakes + 1.59)*0.15)
    TC = "Rs" , str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)
    
    a1 = int(E_Latta.get())
    a2 = int(E_Coke.get())
    a3 = int(E_Iced_Latta.get())
    a4 = int(E_Coffee.get())
    a5 = int(E_Cappuccin.get())
    a6 = int(E_Tea.get())
    a7 =int(E_Cold_coffee.get())
    a8 =int(E_Beer.get())
    a9 =int(E_Coffee_cake.get())
    a10 =int(E_Black_forest.get())
    a11 =int(E_Cream_cake.get())
    a12 =int(E_Lagoos_cake.get())
    a13 =int(E_Fruit_cake.get())
    a14 =int(E_Chocolate_cake.get())
    a15 =int(E_Chocolava.get())
    a16 =int(E_Bread_cake.get())
    a17 =int(E_Menu_Of_Day1.get())
    a18 =int(E_Menu_Of_Day2.get())
    a19 =int(E_Season_Special_1.get())
    a20 =int(E_Season_Special_2.get())
    
    txtReceipt.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t\t'+ DateofOrder.get()+"\n")
    txtReceipt.insert(END,'===============================================\n'+
                      'Items\t\t\t'+"Count of Items \n"+
                      '-------------------------------------------------------------------------------------\n')
    while a1 > 0:  
        txtReceipt.insert(END,'Latta:\t\t\t\t'+ E_Latta.get()+"\n")
        break
    while a2 > 0:        
        txtReceipt.insert(END,'Coke:\t\t\t\t'+ E_Coke.get()+"\n")
        break
    while a3 > 0:        
        txtReceipt.insert(END,'Iced_Latta:\t\t\t\t'+ E_Iced_Latta.get()+"\n")
        break
    while a4 > 0:     
        txtReceipt.insert(END,'Coffee:\t\t\t\t'+ E_Coffee.get()+"\n")
        break
    while a5 > 0:      
        txtReceipt.insert(END,'Cappuccin:\t\t\t\t'+ E_Cappuccin.get()+"\n")
        break
    while a6 > 0:
        txtReceipt.insert(END,'Tea:\t\t\t\t'+ E_Tea.get()+"\n")
        break
    while a7 > 0:
        txtReceipt.insert(END,'Cold_coffee:\t\t\t\t'+ E_Cold_coffee.get()+"\n")
        break
    while a8 > 0:        
        txtReceipt.insert(END,'Beer:\t\t\t\t'+ E_Beer.get()+"\n")
        break
    while a9 > 0:
        txtReceipt.insert(END,'Coffee_cake:\t\t\t\t'+ E_Coffee_cake.get()+"\n")
        break
    while a10 > 0:
        txtReceipt.insert(END,'Black_forest:\t\t\t\t'+ E_Black_forest.get()+"\n")
        break
    while a11 > 0:
        txtReceipt.insert(END,'Cream_cake:\t\t\t\t'+ E_Cream_cake.get()+"\n")
        break
    while a12 > 0:
        txtReceipt.insert(END,'Lagoos_cake:\t\t\t\t'+E_Lagoos_cake.get()+"\n")
        break
    while a13 > 0:
        txtReceipt.insert(END,'Fruit_cake:\t\t\t\t'+ E_Fruit_cake.get()+"\n")
        break
    while a14 > 0:
        txtReceipt.insert(END,'Chocolate_cake:\t\t\t\t'+ E_Chocolate_cake.get()+"\n")
        break
    while a15 > 0:
        txtReceipt.insert(END,'Chocolava:\t\t\t\t'+ E_Chocolava.get()+"\n")
        break
    while a16 > 0:
        txtReceipt.insert(END,'Bread_cake:\t\t\t\t'+ E_Bread_cake.get()+"\n")
        break
    while a17 > 0:
        txtReceipt.insert(END,'Menu_Of_Day_1:\t\t\t\t'+ E_Menu_Of_Day1.get()+"\n")
        break
    while a18 > 0:
        txtReceipt.insert(END,'Menu_Of_Day_2:\t\t\t\t'+ E_Menu_Of_Day2.get()+"\n")
        break
    while a19 > 0:
        txtReceipt.insert(END,'Season_Special_1:\t\t\t\t'+ E_Season_Special_1.get()+"\n")
        break
    while a20 > 0:
        txtReceipt.insert(END,'Season_Special_2:\t\t\t\t'+ E_Season_Special_2.get()+"\n")
        break
    
    txtReceipt.insert(END,'\n===============================================\n' + 'Tax Paid:\t\t' + PaidTax.get() +"\n")
    txtReceipt.insert(END,'Service Charge:\t\t'+ ServiceCharge.get()+'\nSubTotal:\t\t' +SubTotal.get() +"\n")
    txtReceipt.insert(END,'===============================================\n'+ 'Total Cost:\t\t' + TotalCost.get() +"\n===============================================\n")

#=======================================================METHODS=======================================================================
def Stats():
    
    r= Tk()
    r.geometry("1600x8000")
    r.title("fidddlestick's cafe management")
    r.configure(background='#5F755E')
    
    txtmgm = Text(r,font=('arial',11,'bold'),bd=8,width=150,height=50,bg="white")
    txtmgm.grid(row = 1, column = 1)
    
    r.mainloop()
    
    
    
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    
    E_Latta.set("0")
    E_Coke.set("0")
    E_Iced_Latta.set("0")
    E_Coffee.set("0")
    E_Cappuccin.set("0")
    E_Tea.set("0")
    E_Cold_coffee.set("0")
    E_Beer.set("0")

    E_Coffee_cake.set("0")
    E_Black_forest.set("0")
    E_Cream_cake.set("0")
    E_Lagoos_cake.set("0")
    E_Fruit_cake.set("0")
    E_Chocolate_cake.set("0")
    E_Chocolava.set("0")
    E_Bread_cake.set("0")
    
    E_Menu_Of_Day1.set('0')
    E_Menu_Of_Day2.set('0')
    E_Season_Special_1.set('0')
    E_Season_Special_2.set('0')

             
    var1.set(0)    
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)

    txtLatta.configure(state=DISABLED)
    txtCoke.configure(state=DISABLED)
    txtIced_Latta.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtCappuccin.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtCold_coffee.configure(state=DISABLED)
    txtBeer.configure(state=DISABLED)
    txtCoffee_cake.configure(state=DISABLED)
    txtBlack_forest.configure(state=DISABLED)
    txtCream_cake.configure(state=DISABLED)
    txtLagoos_cake.configure(state=DISABLED)
    txtFruit_cake.configure(state=DISABLED)
    txtChocolate_cake.configure(state=DISABLED)
    txtChocolava.configure(state=DISABLED)
    txtBread_cake.configure(state=DISABLED)
    txtMen1.configure(state=DISABLED)
    txtMen2.configure(state=DISABLED)
    txtSp1.configure(state=DISABLED)
    txtSp2.configure(state=DISABLED)
    
def goback():
    root.destroy()

#=========================================================================CHECKBOX==========================================================================

def chkbutton_value():
    if (var1.get() == 1):
        txtLatta.configure(state= NORMAL)
    elif var1.get()== 0:
            txtLatta.configure(state= DISABLED)
            E_Latta.set("0")
    if (var2.get() == 1):
        txtCoke.configure(state=NORMAL)
    elif var2.get()== 0:
            txtCoke.configure(state=DISABLED)
            E_Coke.set("0")
    if (var3.get() == 1):
        txtIced_Latta.configure(state=NORMAL)
    elif var3.get()== 0:
            txtIced_Latta.configure(state=DISABLED)
            E_Iced_Latta.set("0")
    if (var4.get() == 1):
        txtCoffee.configure(state=NORMAL)
    elif var4.get()== 0:
            txtCoffee.configure(state=DISABLED)
            E_Coffee.set("0")
    if (var5.get() == 1):
        txtCappuccin.configure(state=NORMAL)
    elif var5.get()== 0:
            txtCappuccin.configure(state=DISABLED)
            E_Cappuccin.set("0")
    if (var6.get() == 1):
        txtTea.configure(state=NORMAL)
    elif var6.get()== 0:
            txtTea.configure(state=DISABLED)
            E_Tea.set("0")
    if (var7.get() == 1):
        txtCold_coffee.configure(state=NORMAL)
    elif var7.get()== 0:
            txtCold_coffee.configure(state=DISABLED)
            E_Cold_coffee.set("0")
    if (var8.get() == 1):
        txtBeer.configure(state=NORMAL)
    elif var8.get()==0:
            txtBeer.configure(state=DISABLED)
            E_Beer.set("0")
    if (var9.get() == 1):
        txtCoffee_cake.configure(state=NORMAL)
    elif var9.get()== 0:
            txtCoffee_cake.configure(state=DISABLED)
            E_Coffee_cake.set("0")
    if (var10.get() == 1):
        txtBlack_forest.configure(state=NORMAL)
    elif var10.get()== 0:
            txtBlack_forest.configure(state=DISABLED)
            E_Black_forest.set("0")
    if (var11.get() == 1):
        txtCream_cake.configure(state=NORMAL)
    elif var11.get()== 0:
            txtCream_cake.configure(state=DISABLED)
            E_Cream_cake.set("0")
    if (var12.get() == 1):
        txtLagoos_cake.configure(state=NORMAL)
    elif var12.get()== 0:
            txtLagoos_cake.configure(state=DISABLED)
            E_Lagoos_cake.set("0")
    if (var13.get() == 1):
        txtFruit_cake.configure(state=NORMAL)
    elif var13.get()== 0:
            txtFruit_cake.configure(state=DISABLED)
            E_Fruit_cake.set("0")
    if (var14.get() == 1):
        txtChocolate_cake.configure(state=NORMAL)
    elif var14.get()== 0:
            txtChocolate_cake.configure(state=DISABLED)
            E_Chocolate_cake.set("0")
    if (var15.get() == 1):
        txtChocolava.configure(state=NORMAL)
    elif var15.get()== 0:
            txtChocolava.configure(state=DISABLED)
            E_Chocolava.set("0")
    if (var16.get() == 1):
        txtBread_cake.configure(state=NORMAL)
    elif var16.get()== 0:
            txtBread_cake.configure(state=DISABLED)
            E_Bread_cake.set("0")
    if (var17.get() == 1):
        txtMen1.configure(state=NORMAL)
    elif var17.get()== 0:
            txtMen1.configure(state=DISABLED)
            E_Menu_Of_Day1.set("0")
    if (var18.get() == 1):
        txtMen2.configure(state=NORMAL)
    elif var18.get()== 0:
            txtMen2.configure(state=DISABLED)
            E_Menu_Of_Day2.set("0")
    if (var19.get() == 1):
        txtSp1.configure(state=NORMAL)
    elif var19.get()== 0:
            txtSp1.configure(state=DISABLED)
            E_Season_Special_1.set("0")
    if (var20.get() == 1):
        txtSp2.configure(state=NORMAL)
    elif var20.get()== 0:
            txtSp2.configure(state=DISABLED)
            E_Season_Special_2.set("0")
  
	
#==========================================================VARIABLES===============================================================================
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
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofCakes=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()


E_Latta=StringVar()
E_Coke=StringVar()
E_Iced_Latta=StringVar()
E_Coffee=StringVar()
E_Cappuccin=StringVar()
E_Tea=StringVar()
E_Cold_coffee=StringVar()
E_Beer=StringVar()

E_Coffee_cake=StringVar()
E_Black_forest=StringVar()
E_Cream_cake=StringVar()
E_Lagoos_cake=StringVar()
E_Fruit_cake=StringVar()
E_Chocolate_cake=StringVar()
E_Chocolava=StringVar()
E_Bread_cake=StringVar()

E_Menu_Of_Day1 = StringVar()
E_Menu_Of_Day2 = StringVar()
E_Season_Special_1 = StringVar()
E_Season_Special_2 = StringVar()

E_Latta.set("0")
E_Coke.set("0")
E_Iced_Latta.set("0")
E_Coffee.set("0")
E_Cappuccin.set("0")
E_Tea.set("0")
E_Cold_coffee.set("0")
E_Beer.set("0")

E_Coffee_cake.set("0")
E_Black_forest.set("0")
E_Cream_cake.set("0")
E_Lagoos_cake.set("0")
E_Fruit_cake.set("0")
E_Chocolate_cake.set("0")
E_Chocolava.set("0")
E_Bread_cake.set("0")

E_Menu_Of_Day1.set('0')
E_Menu_Of_Day2.set('0')
E_Season_Special_1.set('0')
E_Season_Special_2.set('0')

DateofOrder.set(time.strftime("%d/%m/%y"))

#=================================================DRINKS===================================================================================================================

Latta = Checkbutton(f1aa, text="  Latta \t\t", variable=var1, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

Coke = Checkbutton(f1aa, text="  Coke \t\t", variable=var2, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

Iced_Latta = Checkbutton(f1aa, text="  Iced_Latta \t\t", variable=var3, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

Coffee = Checkbutton(f1aa, text="  Coffee \t\t", variable=var4, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

Cappuccino = Checkbutton(f1aa, text="  Cappuccino \t\t", variable=var5, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

Tea = Checkbutton(f1aa, text="  Tea \t\t", variable=var6, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

Cold_coffee = Checkbutton(f1aa, text="  Cold_coffee \t\t", variable=var7, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

Beer = Checkbutton(f1aa, text="  Beer \t\t", variable=var8, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

MOD1 = Checkbutton(f1aa, text="  Season Special 1 \t\t", variable=var19, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=8,sticky=W)

MOD2 = Checkbutton(f1aa, text="  Season Special 2 \t\t", variable=var20, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=9,sticky=W)



#====================================================CAKES======================================================================================================================

Coffee_cake = Checkbutton(f1ab, text=" Coffee_cake \t\t\t", variable=var9, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

Black_forest = Checkbutton(f1ab, text=" Black_forest \t\t\t", variable=var10, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

Cream_cake = Checkbutton(f1ab, text=" Cream_cake \t\t\t", variable=var11, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

Lagoos_cake = Checkbutton(f1ab, text=" Lagoos_cake \t\t\t", variable=var12, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

Fruit_cake = Checkbutton(f1ab, text=" Fruit_cake \t\t\t", variable=var13, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

Chocolate_cake = Checkbutton(f1ab, text=" Chocolate_cake \t\t\t", variable=var14, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

Chocolava = Checkbutton(f1ab, text=" Chocolava \t\t\t", variable=var15, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

Bread_cake = Checkbutton(f1ab, text=" Bread_cake \t\t\t", variable=var16, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

MOD1 = Checkbutton(f1ab, text="  Menu Of The day 1 \t\t", variable=var17, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=8,sticky=W)

MOD2 = Checkbutton(f1ab, text="  Menu Of The Day 2 \t\t", variable=var18, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=9,sticky=W)

#=====================================================ENTER WIDGE DRINKS================================================================================================================

txtLatta = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Latta, state=DISABLED)
txtLatta.grid(row=0,column=1)

txtCoke = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Coke, state=DISABLED)
txtCoke.grid(row=1,column=1)

txtIced_Latta = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Iced_Latta,state=DISABLED)
txtIced_Latta.grid(row=2,column=1)

txtCoffee = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Coffee,state=DISABLED)
txtCoffee.grid(row=3,column=1)

txtCappuccin = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cappuccin,state=DISABLED)
txtCappuccin.grid(row=4,column=1)

txtTea = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Tea,state=DISABLED)
txtTea.grid(row=5,column=1)

txtCold_coffee = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cold_coffee,state=DISABLED)
txtCold_coffee.grid(row=6,column=1)

txtBeer = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Beer,state=DISABLED)
txtBeer.grid(row=7,column=1)

txtSp1 = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Season_Special_1,state=DISABLED)
txtSp1.grid(row=8,column=1)

txtSp2 = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Season_Special_2,state=DISABLED)
txtSp2.grid(row=9,column=1)



#=====================================================ENTER WIDGE CAKES========================================================================================

txtCoffee_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Coffee_cake,state=DISABLED)
txtCoffee_cake.grid(row=0,column=1)

txtBlack_forest = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Black_forest,state=DISABLED)
txtBlack_forest.grid(row=1,column=1)

txtCream_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cream_cake,state=DISABLED)
txtCream_cake.grid(row=2,column=1)

txtLagoos_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Lagoos_cake,state=DISABLED)
txtLagoos_cake.grid(row=3,column=1)

txtFruit_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Fruit_cake,state=DISABLED)
txtFruit_cake.grid(row=4,column=1)

txtChocolate_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Chocolate_cake,state=DISABLED)
txtChocolate_cake.grid(row=5,column=1)

txtChocolava = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Chocolava,state=DISABLED)
txtChocolava.grid(row=6,column=1)

txtBread_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Bread_cake,state=DISABLED)
txtBread_cake.grid(row=7,column=1)

txtMen1 = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Menu_Of_Day1,state=DISABLED)
txtMen1.grid(row=8,column=1)

txtMen2 = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Menu_Of_Day2,state=DISABLED)
txtMen2.grid(row=9,column=1)

#===========================================================INFORMATION==========================================================================================

lblReceipt = Label(ft2,font=('arial',16,'bold'),text="Get Receipt:",bd=2,anchor='w')
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt = Text(ft2,font=('arial',11,'bold'),bd=8,width=59,height=22,bg="white")
txtReceipt.grid(row=1,column=0)

#============================================================BUTTONS=============================================================================================

btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Total",command=CostofItems).grid(row=0,column=0)

#btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Receipt",command=Receipt).grid(row=0,column=1)

btnReset=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Reset",command=Reset).grid(row=0,column=2)

btnExit=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Exit",command=goback).grid(row=0,column=3)



root.mainloop()
