#import mysql.connector

from cx_Oracle import *
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Button
from tkinter import messagebox


user="2018BCGRP30/Na387@XEPDB1"

con= connect('2018BCGRP30/Na387@XEPDB1')
cur = con.cursor()

cur.execute("SELECT * FROM EMPLOYEES")

for i in cur:
    print(i)

root=Tk()
root.geometry('400x350')
root.title("Employee registration system")
root.configure(bg="black")


def add_employee(): # new window definition
    def add_query():
        global root
        Eid = E1.get()
        Fname = E2.get()
        Lname = E3.get()
        cur.execute("SELECT EID, COUNT(*) FROM EMPLOYEES WHERE EID = '"+Eid+"' GROUP BY EID")
        results = cur.fetchall()
        row_count = cur.rowcount
        if(row_count > 0):
       		messagebox.showwarning("ERROR", "EMPLOYEE Already Exists")
       		return
        stat="INSERT INTO EMPLOYEES(Eid,Fname,Lname) VALUES ('"+Eid+"','"+Fname+"','"+Lname+"')"
        
        cur.execute(stat)
        con.commit()
       # mydb.commit()
        add.config(state=NORMAL)
        update.config(state=NORMAL)
        show.config(state=NORMAL)
        delete.config(state=NORMAL)
        newwin.destroy()
    newwin = Toplevel(root)
    newwin.geometry('400x350')
    newwin.configure(bg='blue')
   # add.config(state=DISABLED)
    newwin.title("Add New Employee")
    L1 = Label(newwin, text="Employee ID",fg = "purple")
    L1.place(x=5,y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=150,y=50)
    L2 = Label(newwin, text="Employee first name", fg = "purple")
    L2.place(x=5,y=100)
    E2 = Entry(newwin, bd=5)
    E2.place(x=150,y=100)
    L3 = Label(newwin, text="Employee last name",fg = "purple")
    L3.place(x=5,y=150)
    E3 = Entry(newwin, bd=5)
    E3.place(x=150,y=150)
    common_img = PhotoImage(width=1,height=1)
    sub=Button(newwin,text="Submit",image=common_img,width=20,compound='c',command=add_query)
    sub.place(x=150,y=200)
    

def del_data():
    def delete():
        global root
        stat="DELETE FROM EMPLOYEES WHERE EID='"+E1.get()+"'"

        cur.execute(stat)
        #mydb.commit()
        con.commit()
        add.config(state=NORMAL)
        newwin.destroy()

    newwin=Toplevel(root)
    newwin.geometry('400x350')
    newwin.configure(bg='blue')
    newwin.title("Delete EMPLOYEES")
    add.config(state=NORMAL)
    L1 = Label(newwin, text="EID")
    L1.place(x=10, y=50)
    E1 = Entry(newwin,bd=5)
    E1.place(x=150, y=50)
    sub = Button(newwin, text="Delete Entry", command=delete)
    sub.place(x=120, y=200)

def update_data():
    def UPDD():
        global root
        stat="UPDATE EMPLOYEES SET LNAME = '"+E1.get()+"' WHERE EID ='"+E2.get()+"'"
        con.commit()
       # mydb.commit()
        cur.execute(stat)
       # mydb.commit()
        con.commit()
        add.config(state=NORMAL)
        newwin.destroy()

    newwin = Toplevel(root)
    newwin.geometry('400x350')
    newwin.configure(bg='blue')
    newwin.title("Update Employee")
    add.config(state=NORMAL)

    L1 = Label(newwin, text="Employee's Last Name")
    L1.place(x=10,y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=150,y=50)

    L2 = Label(newwin, text="Employee ID")
    L2.place(x=10,y=100)
    E2 = Entry(newwin, bd=5)
    E2.place(x=150,y=100)

    sub=Button(newwin,text="Update",command=UPDD)
    sub.place(x=120,y=200)

def display():
    newwin=Toplevel(root)
    newwin.geometry('400x350')

   
   
    stat="SELECT * FROM EMPLOYEES ORDER BY Eid ASC"
    cur.execute(stat)
    L1=Label(newwin,text="Employee's ID")
    L1.grid(row=0,column=0)
    L2 = Label(newwin, text="Employee's First Name")
    L2.grid(row=0, column=1)
    L3=Label(newwin,text="Employee's Last Name")
    L3.grid(row=0,column=2)
    
    i=1
    for row in cur:
        L1 = Label(newwin, text=row[0])
        L1.grid(row=i, column=0)
        L2 = Label(newwin, text=row[1])
        L2.grid(row=i, column=1)
        L3 = Label(newwin, text=row[2])
        L3.grid(row=i, column=2)
        i+=1

add= Button(root,text='Add New Employee',command=add_employee)
delete= Button(root,text='Delete Employee Entry',command=del_data)
update= Button(root,text='Update Employee Info',command=update_data)
show= Button(root,text='Show Employee Details',command=display)

add.place(x=50,y=50)
delete.place(x=150,y=100)
update.place(x=50,y=150)
show.place(x=150,y=200)

root.mainloop()

print("Hello world")