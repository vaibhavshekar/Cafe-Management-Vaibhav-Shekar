from tkinter import*
import random
import time;
import datetime
import mysql.connector as contr
import pandas as pd

mydb = contr.connect(
  host="localhost",
  user="root",
  password="123456",
  database="Cafe_Management"
)
global mycursor
mycursor = mydb.cursor()

r= Tk()
r.geometry("1600x8000")
r.title("fidddlestick's cafe management")
r.configure(background='#5F755E')
 
txtmgm = Text(r,font=('arial',11,'bold'),bd=8,width=100,height=10,bg="white")
txtmgm.grid(row = 1, column = 1)

#global usr_inp 
#usr_inp = 

global w


search1 = IntVar()
search2 = StringVar()
search3 = IntVar()
search4 = StringVar()
search5 = StringVar()
search6 = IntVar()
v = StringVar()
SRCH = StringVar()


def empl_dets():
    
    mycursor.execute("SELECT * FROM empl_dets")

    myresult = mycursor.fetchall()

    #for x in myresult:
        #txtmgm.insert(END,x)

    sl = pd.read_sql_query("select * from empl_dets",mydb)
    df1 = pd.DataFrame(sl)
    df1.to_csv('E:\Cafe Management\Employee details.csv')
    rd = pd.read_csv('E:\Cafe Management\Employee details.csv', usecols = ['empl_id','name','phone_number','Post','Date_Of_Join','salary'])
    txtmgm.insert(INSERT, rd)
    txtmgm.insert(END,'\n'+'\n')
    

def add_empl():
    sql = "INSERT INTO empl_dets('empl_id','name','phone_number','Post','Date_Of_Join','salary') VALUES (%s,%s,%s,%s,%s,%s)"
    val = tuple((1112,'John',9999999999,'cashier','2021-09-05', 25000))
    mycursor.execute(sql,val)

    mydb.commit()
  

      
def srch_empl():
    s = Tk()
    s.geometry('400x400')
    s.configure(background='light blue')
    
    def exit_srch():
        s.destroy()
        
    def srching():       
        
        srch = pd.read_csv('E:\Cafe Management\Employee details.csv', usecols = ['empl_id','name','phone_number','Post','Date_Of_Join','salary'])
        df_srch = pd.DataFrame(srch)
        
        if len(search1)>0:       
            srch_sel = df_srch.loc[df_srch[v]]
        elif len(search2)>0:
            srch_sel = df_srch.loc[df_srch[v]]
        elif len(search3)>0:
            srch_sel = df_srch.loc[df_srch[v]]
        elif len(search4)>0:       
            srch_sel = df_srch.loc[df_srch[v]]
        elif len(search5)>0:       
            srch_sel = df_srch.loc[df_srch[v]]
        elif len(search6)>0:       
            srch_sel = df_srch.loc[df_srch[v]]
        srchtxt.insert(END,srch_sel.get())
        
    Label(s,text='').pack()
    Label(s,text='Enter your search').pack()
    Entry(s,textvariable = SRCH).pack()
    Radiobutton(s, text = 'Employee Id', value = 1, textvariable = search1, background = "light blue").pack()
    Radiobutton(s, text = 'Name', value = 2, textvariable = search2, background = "light blue").pack()
    Radiobutton(s, text = 'Phone Number', value = 3, textvariable = search3, background = "light blue").pack()
    Radiobutton(s, text = 'Post', value = 4, textvariable = search4, background = "light blue").pack()
    Radiobutton(s, text = 'Date Of Join', value = 5, textvariable = search5, background = "light blue").pack()   
    Radiobutton(s, text = 'Salary', value = 6, textvariable = search6, background = "light blue").pack() 
    
    
    Button(s,text='OK',command=srching).pack()
    srchtxt= Text(s,font=('arial',11,'bold'),bd=8,width=19,height=9,bg="white").pack()
    
     #exit_btn = Button(s,fg="black",font=('arial',16,'bold'),width=7,text="exit",command=exit_srch).grid(row=4,column=2)
    
    
    
def popupwin():
    w = Tk()
    w.geometry('400x400')
    w.configure(background='#5F755E')
    
    def exit_srch():
        w.destroy()
        
    exit_btn = Button(w,fg="black",font=('arial',16,'bold'),width=7,text="exit",command=exit_srch).grid(row=4,column=2)
    w.mainloop()

def exit_mgm():
    w = Tk()
    try:       
        w.destroy()
        r.destroy()
    except:
        r.destroy()
    
def exit_srch():
    w.destroy()
    
    
    

fetch_empl_btn = Button(r,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=7,text="Empl Details",command=empl_dets).grid(row=6,column=12)
add_emp_btn = Button(r,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=7,text="add empl",command=add_empl).grid(row=8,column=13)
srch_empl_btn = Button(r,fg="black",font=('arial',16,'bold'),width=7,text="search",command=srch_empl).grid(row=10,column=14)
exit_btn = Button(r,fg="black",font=('arial',16,'bold'),width=7,text="exit",command=exit_mgm).grid(row=12,column=16)
r.mainloop()