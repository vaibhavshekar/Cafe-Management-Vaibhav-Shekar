from tkinter import *
from datetime import datetime
import tkinter as tk 
import mysql.connector as contr
import pandas as pd
import csv 
  
root=tk.Tk() 
root.geometry("600x400")
card_var=StringVar()
  
def submit():

    cardno=card_var.get()
    timestamp = str(datetime.now())
    data = [cardno,timestamp]
    df1 = pd.read_csv('E:\Cafe Management\saved cards.csv',usecols = ['card number'])
    lst = df1['card number'].tolist()
    intcdno = int(cardno)
    if (intcdno in lst):        
        df = pd.read_csv('E:\Cafe Management\punch.csv',usecols = ['card number','punch details',])
        df2 = pd.DataFrame({'card number':[cardno],'punch details':[timestamp]})
        df3 = df.append(df2,ignore_index = True)
        df3.to_csv('E:\Cafe Management\punch.csv',index=False)
        card_var.set("")
    else:
        messagebox.showerror("showerror", "Error: Invalid Card number")

        card_var.set("")
    
    root.destroy()
    
    
     
name_label = tk.Label(root, text = 'CARD Number', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = card_var, font=('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit) 
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()
