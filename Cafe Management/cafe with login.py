from tkinter import *
from datetime import datetime
import tkinter as tk 
import mysql.connector as contr
import pandas as pd
import csv 
  
r1=tk.Tk() 
r1.geometry("600x400")
r1.configure(bg='#CC9966')
#r1.attributes('-fullscreen', True)
card_var=StringVar()
  
def submit():

    cardno=card_var.get()
    timestamp = str(datetime.now())
    data = [cardno,timestamp]
    
#========== checking if the entered card no is a valid one=====================================================

    df1 = pd.read_csv('E:\Cafe Management\saved cards.csv',usecols = ['card number'])
    lst = df1['card number'].tolist()
    intcdno = int(cardno)
    if (intcdno in lst):        
        df = pd.read_csv('E:\Cafe Management\punch.csv',usecols = ['card number','punch details',])
        df2 = pd.DataFrame({'card number':[cardno],'punch details':[timestamp]})
        df3 = df.append(df2,ignore_index = True)
        df3.to_csv('E:\Cafe Management\punch.csv',index=False)
        card_var.set("")
        r1.destroy()
        execfile('E:\Cafe Management\CAFE FINAL 1.py')
        
#=================== error for wrong card number ==========================================================================
       
    else:
        messagebox.showerror("showerror", "Error: Invalid Card number")
        card_var.set("")
        
def ext():
    r1.destroy()
    
name_label = tk.Label(r1, text = 'CARD Number', font=('calibre',16, 'bold')).pack()
name_entry = tk.Entry(r1,textvariable = card_var, font=('calibre',16,'normal')).pack()
sub_btn=tk.Button(r1,text = 'Submit', command = submit).pack()
ext_btn = tk.Button(r1, text = 'exit', command = ext).pack()
#name_label.grid(row=0,column=0)
#name_entry.grid(row=0,column=1)
#sub_btn.grid(row=2,column=1)
#ext_btn.grid(row=2,column=2)

r1.mainloop()