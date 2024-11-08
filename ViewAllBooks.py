from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkfont
import mysql.connector as mysql
import csv
import os
import time

def booksFile():
    f=open("BOOKS.CSV","w",newline="\n")
    L=["BOOK ID","TITLE","AUTHOR","STATUS"]
    w=csv.writer(f)
    w.writerow(L)
    L=[]
    getBooks = "select * from "+bookTable
    try:
        con.commit()
        cur.execute(getBooks)
        rows = cur.fetchall()    
        for row in rows:
            L=list(row)
            w.writerow(L)
        f.close()
        filename = "BOOKS.CSV"
        os.system(filename)
    except:
        messagebox.showinfo("Notification","Failed to fetch files from database")
    
def viewall():

    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
        
    global mypass,mydatabase,con,cur,root1,bookTable
    
    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase="db"

    con = mysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" 
    
    root1 = Tk()
    root1.title("Library")
    root1.minsize(width=400,height=400)
    root1.geometry("872x700")


    Canvas1 = Canvas(root1) 
    Canvas1.config(bg="light sky blue")
    Canvas1.pack(expand=True,fill=BOTH)

    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.01,rely=0.375,relwidth=0.96,relheight=0.5)
    sb = Scrollbar(labelFrame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    
    tree = ttk.Treeview(labelFrame, column=("c1", "c2", "c3", "c4"), show='headings')
    style = ttk.Style(root1)
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="lemon chiffon", foreground="purple1", font=('Courier', 15,'bold'))
    style.configure("Treeview", background="light green", font=('Courier', 12,'bold'))
    
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="BID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="TITLE")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="AUTHOR")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="STATUS")

    # Treeview Column Formate
    tree.column('#1', width=50, anchor=CENTER)
    tree.column('#2', width=300, anchor=W)
    tree.column('#3', width=150, anchor=W)
    tree.column('#4', width=120, anchor=CENTER)
    tree.place(relx=0.01,rely=0.1,relwidth=0.96,relheight=0.8)

    tree.config(yscrollcommand=sb.set)
    sb.config(command=tree.yview)

    calanderimg = PhotoImage(file='Calendar.png', master=root1)
    calanderimg = calanderimg.subsample(1,1)

    clockimg = PhotoImage(file='Clock.png', master=root1)
    clockimg = clockimg.subsample(1,1)

    headingFrame1 = Frame(root1,bg="black", bd=5)
    headingFrame1.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.1)

    headingLabel = Label(headingFrame1, text="DAV LIBRARY", bg='light sea green', fg='midnight blue', font=('Courier',26,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    dateFrame = Frame(root1, bg="black", bd=3)
    dateFrame.place(relx=0.15,rely=0.18, relwidth=0.355, relheight=0.075)

    dateLabel = Label(dateFrame,image = calanderimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    dateLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    date_string = time.strftime("%d/%m/%Y")
    dateLabel.configure(text=" Date : " + date_string)

    timeFrame = Frame(root1, bg="black", bd=3)
    timeFrame.place(relx=0.525,rely=0.18, relwidth=0.325, relheight=0.075)

    clocktimLabel = Label(timeFrame,image = clockimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    clocktimLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    Date_Tim()
          
    headingFrame2 = Frame(root1,bg="#FFBB00",bd=5)
    headingFrame2.place(relx=0.25,rely=0.28,relwidth=0.5,relheight=0.08)
        
    headingLabel1 = Label(headingFrame2, text="View All Books", bg='black', fg='white', font=('Courier',26,'bold','italic'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)
    
        
    getBooks = "select * from "+bookTable
    try:
        con.commit()
        cur.execute(getBooks)
        rows = cur.fetchall()    
        for row in rows:
            tree.insert("", tk.END, values=row)        
    except:
        messagebox.showinfo("Notification","Failed to fetch files from database")

    fileBtn = Button(root1,text="EXCEL FILE",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=booksFile)
    fileBtn.place(relx=0.25,rely=0.9, relwidth=0.18,relheight=0.08)        
    
    quitBtn = Button(root1,text="QUIT",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=root1.destroy)
    quitBtn.place(relx=0.55,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root1.mainloop()
#viewall()
