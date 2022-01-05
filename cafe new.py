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

f1 = Frame(root, width=700,height=750,bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width=340,height=750,bd=8, relief="raise")
f2.pack(side=RIGHT)

ft2 = Frame(f2, width=340,height=450,bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=340,height=250,bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1a = Frame(f1, width=700,height=430,bd=8, relief="raise")
f1a.pack(side=TOP)
# f2a = Frame(f1, width=900,height=320,bd=6, relief="raise")
# f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width = 300, height=630,bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width = 300, height=630,bd=16, relief="raise")
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


E_cappuccino=StringVar()
E_americano=StringVar()
E_Cold_Brew=StringVar()
E_CCMff=StringVar()
E_Sr_Smoothie=StringVar()
E_SOF=StringVar()
E_COF=StringVar()
E_DCF=StringVar()

E_Cold_Brew_FV=StringVar()
E_CheeseCake=StringVar()
E_HotChoc=StringVar()
E_Waffels=StringVar()
E_MDShake=StringVar()
E_ButterBeer=StringVar()
E_MochaFrappe=StringVar()
E_Latte=StringVar()

E_Menu_Of_Day1 = StringVar()
E_Menu_Of_Day2 = StringVar()
E_Season_Special_1 = StringVar()
E_Season_Special_2 = StringVar()

E_cappuccino.set("0")
E_americano.set("0")
E_Cold_Brew.set("0")
E_CCMff.set("0")
E_Sr_Smoothie.set("0")
E_SOF.set("0")
E_COF.set("0")
E_DCF.set("0")

E_Cold_Brew_FV.set("0")
E_CheeseCake.set("0")
E_HotChoc.set("0")
E_Waffels.set("0")
E_MDShake.set("0")
E_ButterBeer.set("0")
E_MochaFrappe.set("0")
E_Latte.set("0")

E_Menu_Of_Day1.set('0')
E_Menu_Of_Day2.set('0')
E_Season_Special_1.set('0')
E_Season_Special_2.set('0')

DateofOrder.set(time.strftime("%d/%m/%y"))


#===================================================================COST OF ITEMS=============================================================

def CostofItems():

    Cost1=125
    Cost2=120
    Cost3=110
    Cost4=70
    Cost5=140
    Cost6=150
    Cost7=160
    Cost8=155
    Cost9=120
    Cost10=85
    Cost11=90
    Cost12=150
    Cost13=145
    Cost14=180
    Cost15=135
    Cost16=125
    Cost17 = 140
    Cost18 = 140
    Cost19 = 150
    Cost20 = 150
    
    
    Item1=float(E_cappuccino.get())
    Item2=float(E_americano.get())
    Item3=float(E_Cold_Brew.get())
    Item4=float(E_CCMff.get())
    Item5=float(E_Sr_Smoothie.get())
    Item6=float(E_SOF.get()) 
    Item7=float(E_COF.get())
    Item8=float(E_DCF.get())
    
    Item9=float(E_Cold_Brew_FV.get()) 
    Item10=float(E_CheeseCake.get())
    Item11=float(E_HotChoc.get())
    Item12=float(E_Waffels.get())
    Item13=float(E_MDShake.get())
    Item14=float(E_ButterBeer.get())
    Item15=float(E_MochaFrappe.get())
    Item16=float(E_Latte.get())
    Item17 = float(E_Menu_Of_Day1.get())
    Item18 = float(E_Menu_Of_Day2.get())
    Item19 = float(E_Season_Special_1.get())
    Item20 = float(E_Season_Special_2.get())

    Price = (Item1 * Cost1) + (Item2 * Cost2) + (Item3 * Cost3) + (Item4 * Cost4) + (Item5 * Cost5) + (Item6 * Cost6) + (Item7 * Cost7) + (Item8 * Cost8) + (Item17 * Cost17) + (Item18 * Cost18) + (Item19 * Cost19) + (Item20 * Cost20)+ (Item9 * Cost9) + (Item10 * Cost10) + (Item11 * Cost11) + (Item12 * Cost12) + (Item13 * Cost13) + (Item14 * Cost14) + (Item15 * Cost15) + (Item16 * Cost16)

    SC= "Rs" , str(0.04 * Price)
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs" , str(Price+(0.04 * Price))
    SubTotal.set(SubTotalofITEMS)

    Tax= "Rs" , str(0.11 * Price)
    PaidTax.set(Tax)

    #TT = ((PriceofDrinks + PriceofCakes + 1.59)*0.15)
    TC = "Rs" , str(Price + (0.04 * Price) + (0.11 * Price))
    TotalCost.set(TC)
    
    a1 = int(E_cappuccino.get())
    a2 = int(E_americano.get())
    a3 = int(E_Cold_Brew.get())
    a4 = int(E_CCMff.get())
    a5 = int(E_Sr_Smoothie.get())
    a6 = int(E_SOF.get())
    a7 =int(E_COF.get())
    a8 =int(E_DCF.get())
    a9 =int(E_Cold_Brew_FV.get())
    a10 =int(E_CheeseCake.get())
    a11 =int(E_HotChoc.get())
    a12 =int(E_Waffels.get())
    a13 =int(E_MDShake.get())
    a14 =int(E_ButterBeer.get())
    a15 =int(E_MochaFrappe.get())
    a16 =int(E_Latte.get())
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
                      'Items\t\t'+'\tRate\t\t'+"Count of Items \n"+
                      '-------------------------------------------------------------------------------------\n')
    while a1 > 0:  
        txtReceipt.insert(END,'Cappuccino:\t\t\t'+ str(Cost1) +'\t\t\t' + E_cappuccino.get()+"\n")
        break
    while a2 > 0:        
        txtReceipt.insert(END,'Americano:\t\t\t'+ str(Cost2) +'\t\t\t' + E_americano.get()+"\n")
        break
    while a3 > 0:        
        txtReceipt.insert(END,'Cold Brew:\t\t\t'+ str(Cost3) +'\t\t\t' + E_Cold_Brew.get()+"\n")
        break
    while a4 > 0:     
        txtReceipt.insert(END,'Chocochip Muffin:\t\t\t'+ str(Cost4) +'\t\t\t' + E_CCMff.get()+"\n")
        break
    while a5 > 0:      
        txtReceipt.insert(END,'Strawberry Smoothie:\t\t\t'+ str(Cost5) +'\t\t\t' + E_Sr_Smoothie.get()+"\n")
        break
    while a6 > 0:
        txtReceipt.insert(END,'Sr oreo Frappe:\t\t\t'+ str(Cost6) +'\t\t\t' + E_SOF.get()+"\n")
        break
    while a7 > 0:
        txtReceipt.insert(END,'Cr Oreo Frappe:\t\t\t'+ str(Cost7) +'\t\t\t' + E_COF.get()+"\n")
        break
    while a8 > 0:        
        txtReceipt.insert(END,'Double Ch Fr:\t\t\t'+ str(Cost8) +'\t\t\t' + E_DCF.get()+"\n")
        break
    while a9 > 0:
        txtReceipt.insert(END,'ColdBrewFV:\t\t\t'+ str(Cost9) +'\t\t\t' + E_Cold_Brew_FV.get()+"\n")
        break
    while a10 > 0:
        txtReceipt.insert(END,'CheeseCake:\t\t\t'+ str(Cost10) +'\t\t\t' + E_CheeseCake.get()+"\n")
        break
    while a11 > 0:
        txtReceipt.insert(END,'Hot Chocolate:\t\t\t'+ str(Cost11) +'\t\t\t' + E_HotChoc.get()+"\n")
        break
    while a12 > 0:
        txtReceipt.insert(END,'Waffels:\t\t\t'+ str(Cost12) +'\t\t\t' +E_Waffels.get()+"\n")
        break
    while a13 > 0:
        txtReceipt.insert(END,'MUDPieShake:\t\t\t'+ str(Cost13) +'\t\t\t' + E_MDShake.get()+"\n")
        break
    while a14 > 0:
        txtReceipt.insert(END,'ButterBeer:\t\t\t'+ str(Cost14) +'\t\t\t' + E_ButterBeer.get()+"\n")
        break
    while a15 > 0:
        txtReceipt.insert(END,'MochaFrappe:\t\t\t'+ str(Cost15) +'\t\t\t' + E_MochaFrappe.get()+"\n")
        break
    while a16 > 0:
        txtReceipt.insert(END,'Latte:\t\t\t'+ str(Cost16) +'\t\t\t' + E_Latte.get()+"\n")
        break
    while a17 > 0:
        txtReceipt.insert(END,'Menu_Of_Day_1:\t\t\t'+ str(Cost17) +'\t\t\t' + E_Menu_Of_Day1.get()+"\n")
        break
    while a18 > 0:
        txtReceipt.insert(END,'Menu_Of_Day_2:\t\t\t'+ str(Cost18) +'\t\t\t' + E_Menu_Of_Day2.get()+"\n")
        break
    while a19 > 0:
        txtReceipt.insert(END,'Season_Special_1:\t\t\t'+ str(Cost19) +'\t\t\t' + E_Season_Special_1.get()+"\n")
        break
    while a20 > 0:
        txtReceipt.insert(END,'Season_Special_2:\t\t\t' + str(Cost20) +'\t\t\t' + E_Season_Special_2.get()+"\n")
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
    
    E_cappuccino.set("0")
    E_americano.set("0")
    E_Cold_Brew.set("0")
    E_CCMff.set("0")
    E_Sr_Smoothie.set("0")
    E_SOF.set("0")
    E_COF.set("0")
    E_DCF.set("0")

    E_Cold_Brew_FV.set("0")
    E_CheeseCake.set("0")
    E_HotChoc.set("0")
    E_Waffels.set("0")
    E_MDShake.set("0")
    E_ButterBeer.set("0")
    E_MochaFrappe.set("0")
    E_Latte.set("0")
    
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

    txtcappuccino.configure(state=DISABLED)
    txtamericano.configure(state=DISABLED)
    txtCold_Brew.configure(state=DISABLED)
    txtCCMff.configure(state=DISABLED)
    txtSr_Smoothie.configure(state=DISABLED)
    txtSOF.configure(state=DISABLED)
    txtCOF.configure(state=DISABLED)
    txtDCF.configure(state=DISABLED)
    txtCold_Brew_FV.configure(state=DISABLED)
    txtCheeseCake.configure(state=DISABLED)
    txtHotChoc.configure(state=DISABLED)
    txtWaffels.configure(state=DISABLED)
    txtMDShake.configure(state=DISABLED)
    txtButterBeer.configure(state=DISABLED)
    txtMochaFrappe.configure(state=DISABLED)
    txtLatte.configure(state=DISABLED)
    txtMen1.configure(state=DISABLED)
    txtMen2.configure(state=DISABLED)
    txtSp1.configure(state=DISABLED)
    txtSp2.configure(state=DISABLED)
    
def goback():
    root.destroy()

#=========================================================================CHECKBOX==========================================================================

def chkbutton_value():
    if (var1.get() == 1):
        txtcappuccino.configure(state= NORMAL)
    elif var1.get()== 0:
            txtcappuccino.configure(state= DISABLED)
            E_cappuccino.set("0")
    if (var2.get() == 1):
        txtamericano.configure(state=NORMAL)
    elif var2.get()== 0:
            txtamericano.configure(state=DISABLED)
            E_americano.set("0")
    if (var3.get() == 1):
        txtCold_Brew.configure(state=NORMAL)
    elif var3.get()== 0:
            txtCold_Brew.configure(state=DISABLED)
            E_Cold_Brew.set("0")
    if (var4.get() == 1):
        txtCold_Brew_FV.configure(state=NORMAL)
    elif var4.get()== 0:
            txtCold_Brew_FV.configure(state=DISABLED)
            E_Cold_Brew_FV.set("0")
    if (var5.get() == 1):
        txtSr_Smoothie.configure(state=NORMAL)
    elif var5.get()== 0:
            txtSr_Smoothie.configure(state=DISABLED)
            E_Sr_Smoothie.set("0")
    if (var6.get() == 1):
        txtSOF.configure(state=NORMAL)
    elif var6.get()== 0:
            txtSOF.configure(state=DISABLED)
            E_SOF.set("0")
    if (var7.get() == 1):
        txtCOF.configure(state=NORMAL)
    elif var7.get()== 0:
            txtCOF.configure(state=DISABLED)
            E_COF.set("0")
    if (var8.get() == 1):
        txtDCF.configure(state=NORMAL)
    elif var8.get()==0:
            txtDCF.configure(state=DISABLED)
            E_DCF.set("0")
    if (var9.get() == 1):
        txtCold_Brew_FV_cake.configure(state=NORMAL)
    elif var9.get()== 0:
            txtCold_Brew_FV_cake.configure(state=DISABLED)
            E_Cold_Brew_FV_cake.set("0")
    if (var10.get() == 1):
        txtCheeseCake.configure(state=NORMAL)
    elif var10.get()== 0:
            txtCheeseCake.configure(state=DISABLED)
            E_CheeseCake.set("0")
    if (var11.get() == 1):
        txtHotChoc.configure(state=NORMAL)
    elif var11.get()== 0:
            txtHotChoc.configure(state=DISABLED)
            E_HotChoc.set("0")
    if (var12.get() == 1):
        txtWaffels.configure(state=NORMAL)
    elif var12.get()== 0:
            txtWaffels.configure(state=DISABLED)
            E_Waffels.set("0")
    if (var13.get() == 1):
        txtMDShake.configure(state=NORMAL)
    elif var13.get()== 0:
            txtMDShake.configure(state=DISABLED)
            E_MDShake.set("0")
    if (var14.get() == 1):
        txtButterBeer.configure(state=NORMAL)
    elif var14.get()== 0:
            txtButterBeer.configure(state=DISABLED)
            E_ButterBeer.set("0")
    if (var15.get() == 1):
        txtMochaFrappe.configure(state=NORMAL)
    elif var15.get()== 0:
            txtMochaFrappe.configure(state=DISABLED)
            E_MochaFrappe.set("0")
    if (var16.get() == 1):
        txtLatte.configure(state=NORMAL)
    elif var16.get()== 0:
            txtLatte.configure(state=DISABLED)
            E_Latte.set("0")
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
  
	

#=================================================DRINKS===================================================================================================================

Capp = Checkbutton(f1aa, text="  Cappuccino\t\t", variable=var1, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

Americano = Checkbutton(f1aa, text="  Americano\t\t", variable=var2, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

Cold_Brew = Checkbutton(f1aa, text="  Cold Brew\t\t", variable=var3, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

Cold_Brew_FV = Checkbutton(f1aa, text="  CC Muffin\t\t", variable=var4, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

Sr_Smoothie = Checkbutton(f1aa, text="  Strawberry Smoothie\t\t", variable=var5, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

SOF = Checkbutton(f1aa, text="  Straberry Oreo Fr\t\t", variable=var6, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

COF = Checkbutton(f1aa, text="  Cr Oreo Fr\t\t", variable=var7, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

DOC = Checkbutton(f1aa, text="  Double Chocolate Fr\t\t", variable=var8, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

MOD1 = Checkbutton(f1aa, text="  Season Special 1\t\t", variable=var19, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=8,sticky=W)

MOD2 = Checkbutton(f1aa, text="  Season Special 2\t\t", variable=var20, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=9,sticky=W)



#====================================================CAKES======================================================================================================================

ColdBrewFV = Checkbutton(f1ab, text=" ColdBrewFV \t\t", variable=var9, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

CheeseCake = Checkbutton(f1ab, text=" CheeseCake \t\t", variable=var10, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

Hot_Chocolate = Checkbutton(f1ab, text=" Hot Chocolate \t\t", variable=var11, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

Waffels = Checkbutton(f1ab, text=" Waffels \t\t", variable=var12, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

MUDPieShake = Checkbutton(f1ab, text=" MUDPie Shake \t\t", variable=var13, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

ButterBeer = Checkbutton(f1ab, text=" ButterBeer \t\t", variable=var14, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

MochaFrappe = Checkbutton(f1ab, text=" MochaFrappe \t\t", variable=var15, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

Latte = Checkbutton(f1ab, text=" Latte \t\t", variable=var16, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

SPP1 = Checkbutton(f1ab, text="  Menu Of The day 1 \t", variable=var17, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=8,sticky=W)

SPP2 = Checkbutton(f1ab, text="  Menu Of The Day 2 \t", variable=var18, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=9,sticky=W)

#=====================================================ENTER WIDGE DRINKS================================================================================================================

txtcappuccino = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_cappuccino, state=DISABLED)
txtcappuccino.grid(row=0,column=1)

txtamericano = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_americano, state=DISABLED)
txtamericano.grid(row=1,column=1)

txtCold_Brew = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cold_Brew,state=DISABLED)
txtCold_Brew.grid(row=2,column=1)

txtCold_Brew_FV = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_CCMff,state=DISABLED)
txtCold_Brew_FV.grid(row=3,column=1)

txtSr_Smoothie = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Sr_Smoothie,state=DISABLED)
txtSr_Smoothie.grid(row=4,column=1)

txtSOF = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_SOF,state=DISABLED)
txtSOF.grid(row=5,column=1)

txtCOF = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_COF,state=DISABLED)
txtCOF.grid(row=6,column=1)

txtDCF = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_DCF,state=DISABLED)
txtDCF.grid(row=7,column=1)

txtSp1 = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Season_Special_1,state=DISABLED)
txtSp1.grid(row=8,column=1)

txtSp2 = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Season_Special_2,state=DISABLED)
txtSp2.grid(row=9,column=1)



#=====================================================ENTER WIDGE CAKES========================================================================================

txtCold_Brew_FV_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cold_Brew_FV,state=DISABLED)
txtCold_Brew_FV_cake.grid(row=0,column=1)

txtCheeseCake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_CheeseCake,state=DISABLED)
txtCheeseCake.grid(row=1,column=1)

txtHotChoc = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_HotChoc,state=DISABLED)
txtHotChoc.grid(row=2,column=1)

txtWaffels = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Waffels,state=DISABLED)
txtWaffels.grid(row=3,column=1)

txtMDShake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_MDShake,state=DISABLED)
txtMDShake.grid(row=4,column=1)

txtButterBeer = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_ButterBeer,state=DISABLED)
txtButterBeer.grid(row=5,column=1)

txtMochaFrappe = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_MochaFrappe,state=DISABLED)
txtMochaFrappe.grid(row=6,column=1)

txtLatte = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Latte,state=DISABLED)
txtLatte.grid(row=7,column=1)

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
