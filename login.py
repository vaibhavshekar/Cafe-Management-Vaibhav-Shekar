# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:08:30 2022

@author: Administrator
"""
from tkinter import *
from datetime import datetime
import tkinter as tk 
import mysql.connector as contr
import pandas as pd
import csv 

mydb = contr.connect(
  host="localhost",
  user="root",
  password="123456",
  database="Cafe_Management"
)

global mycursor
mycursor= mydb.cursor()
  
root=tk.Tk() 
root.geometry("600x400")
  
card_var=tk.StringVar()
  
def submit():
 
    cardno=card_var.get()
    timestamp = str(datetime.now())
    data = [cardno,timestamp]
    df1 = pd.read_csv('E:\Cafe Management\saved cards.csv',usecols = ['card number'])
    exist = cardno in df1
    correct = exist
    if card_var in df1.values :
        df = pd.read_csv('E:\Cafe Management\punch.csv',usecols = ['punch details','card number'])
        df2 = pd.DataFrame(data)
        df3 = df.append(df2,ignore_index = True)
        df3.to_csv('E:\Cafe Management\punch.csv',index=False)
    else:
        messagebox.showerror("showerror", "Error: Invalid Card number")

    card_var.set("")
    
    #root.destroy()
     
name_label = tk.Label(root, text = 'CARD Number', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = card_var, font=('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit) 
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()