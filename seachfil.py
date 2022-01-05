# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 16:50:57 2022

@author: Hiten Dhore
"""

from tkinter import*
import csv
import pandas as pd

root= Tk()
root.geometry("1600x8000")
#Tops = Frame(root, width=1350,height=100,bd=14, relief="raise")
#Tops.pack(side=TOP)


customer_frame = LabelFrame(root,text="Customer Details",font=("arial", 15, "bold"),bg="#fff346", relief=GROOVE)
customer_frame.pack(side=TOP, fill="x")

ntbs = StringVar()
ntbs.set("")
ctbs = StringVar()
ctbs.set("")

customer_name_label = Label(customer_frame, text="Name", font=("arial", 15, "bold"),bg = "#fff346", fg="black")
customer_name_label.grid(row = 0, column = 0)

customer_name_entry = Entry(customer_frame,width=20,font="arial 15",bd=5,textvariable=ntbs)
customer_name_entry.grid(row = 0, column=1,padx=10)

customer_contact_label = Label(customer_frame, text="Contact", font=("arial", 15, "bold"),bg = "#fff346", fg="black")
customer_contact_label.grid(row = 0, column = 2)

customer_contact_entry = Entry(customer_frame,width=20,font="arial 15",bd=5,textvariable=ctbs)
customer_contact_entry.grid(row = 0, column=3,padx=10)

"""
f1 = Frame(root, width=900,height=950,bd=8, relief="raise")
f1.pack(side=LEFT)
ft1 = Frame(f1, width=900,height=750,bd=12, relief="raise") # change size to make fit receipt
ft1.pack(side=TOP)
"""

f2 = Frame(root, width=940,height=650,bd=8, relief="raise")
f2.pack(side=TOP)

ft2 = Frame(f2, width=940,height=450,bd=12, relief="raise") # change size to make fit receipt
ft2.pack(side=TOP)

#billdf = pd.DataFrame()

s="D:/"
def sbtn():
    s1=str(ntbs.get())
    s2=""
    s2=s+s1+".csv"
    bild = pd.read_csv(s2)
    dftbu = bild[bild["Quantity"]>0]
    dftbu.to_csv(s2)
    with open(s2, newline = "") as file:
       reader = csv.reader(file)

       # r and c tell us where to grid the labels
       r = 0
       for col in reader:
          c = 0
          for row in col:
             # i've added some styling
             label = Label(ft2, width = 20, height = 2, text = row)
             label.grid(row = r, column = c)
             c += 1
          r += 1
#    if not os.path.exists(fa):

btnSearch=Button(customer_frame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Display",command=sbtn).grid(row=0,column=4)



# open file

root.mainloop()