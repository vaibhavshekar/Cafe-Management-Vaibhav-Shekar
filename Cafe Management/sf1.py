
from tkinter import*
import csv
import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Cafe_Management")
mycursor=mydb.cursor()

root1= Tk()
root1.geometry("1600x8000")
#Tops = Frame(root1, width=1350,height=100,bd=14, relief="raise")
#Tops.pack(side=TOP)




ntbs = StringVar()
ntbs.set("")
ctbs = StringVar()
ctbs.set("")
btbs = StringVar()
btbs.set("")

customer_frame = LabelFrame(root1,text="Customer Details",font=("arial", 15, "bold"),bg="#fff346", relief=GROOVE)
customer_frame.pack(side=TOP, fill="x")

customer_name_label = Label(customer_frame, text="Name", font=("arial", 15, "bold"),bg = "#fff346", fg="black")
customer_name_label.grid(row = 0, column = 0)

customer_name_entry = Entry(customer_frame,width=20,font="arial 15",bd=5,textvariable=ntbs)
customer_name_entry.grid(row = 0, column=1,padx=10)

customer_contact_label = Label(customer_frame, text="Contact", font=("arial", 15, "bold"),bg = "#fff346", fg="black")
customer_contact_label.grid(row = 0, column = 2)

customer_contact_entry = Entry(customer_frame,width=20,font="arial 15",bd=5,textvariable=ctbs)
customer_contact_entry.grid(row = 0, column=3,padx=10)

bill_number_label = Label(customer_frame, text="bill number", font=("arial", 15, "bold"),bg = "#fff346", fg="black")
bill_number_label.grid(row = 0, column = 4)

bill_number_entry = Entry(customer_frame,width=20,font="arial 15",bd=5,textvariable=btbs)
bill_number_entry.grid(row = 0, column=5,padx=10)


# f1 = Frame(root1, width=900,height=350,bd=8, relief="raise")
# f1.pack(side=LEFT)
ft1 = Frame(root1, width=900,height=350,bd=12, relief="raise") # change size to make fit receipt
ft1.pack(side=RIGHT)


f2 = Frame(root1, width=940,height=650,bd=8, relief="raise")
f2.pack(side=LEFT)
txtsrch = Text(f2,font=('arial',20,'bold'),bd=8,width=59,height=22,bg="white")
txtsrch.pack()

#ft2 = Frame(f2, width=940,height=450,bd=12, relief="raise") # change size to make fit receipt
#ft2.pack(side=LEFT)

#billdf = pd.DataFrame()
def sbn():        # search button
    w1=str(ntbs.get())
    w2 = str(ctbs.get())
    w4 = """SELECT * FROM custdet WHERE CustomerName=(%s) OR ContactNumber=(%s)""" 
    mycursor.execute(w4,(w1,w2))
    for val in mycursor:
        srchval = str(val)
        txtsrch.insert(END,srchval + "\n")
#    mycursor.close() 
#    mycursor = connection.cursor()
#    mydb.commit()

s="E:/Cafe Management/bill records/"

def sbtn():    # to be converted to display button
    s1=str(btbs.get())
    #s3 = str(ctbs.get())
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
             label = Label(ft1, width = 20, height = 2, text = row)
             label.grid(row = r, column = c)
             c += 1
          r += 1
#    if not os.path.exists(fa):

def ext():
    qexit=messagebox.askyesno("Quit System","Do you want to quit?")
    if qexit > 0:
        root1.destroy()
        return
    
def errorbtn():
    messagebox.showerror("showerror", "Error: Invalid Bill Number")
    ntbs.set("")

Searchbtn=Button(customer_frame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Search",command=sbn).grid(row=0,column=6)
displbtn=Button(customer_frame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Display",command=sbtn).grid(row=0,column=7)
extbtn=Button(customer_frame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Exit",command=ext).grid(row=0,column=8)


# open file

root1.mainloop()