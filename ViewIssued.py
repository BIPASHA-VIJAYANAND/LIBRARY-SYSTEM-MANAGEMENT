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

def issuedFile():
    f=open("ISSUED.CSV","w",newline="\n")
    L=["BOOK ID","TITLE","AUTHOR","ISSUED TO","CLASS","SECTION","DATE OF ISSUE"]
    w=csv.writer(f)
    w.writerow(L)
    L=[]
    getBooks = "select "+bookTable+".bid, title, author, issuedto, class, section, dateofissue from "+bookTable+","+issueTable+" where "+bookTable+".bid = "+issueTable+".bid"
    try:
        con.commit()
        cur.execute(getBooks)
        rows = cur.fetchall()    
        for row in rows:
            L=list(row)
            L[6] = L[6].strftime("%d-%m-%y")
            w.writerow(L)
        f.close()
        filename = "ISSUED.CSV"
        os.system(filename)
    except:
        messagebox.showinfo("Notification","Failed to fetch files from database")
    
def viewIssued():
    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
        
    global mypass,mydatabase,con,cur,root2,bookTable,issueTable
    
    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase="db"

    con = mysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    issueTable = "books_issued" #Issue Table
    bookTable = "books" 
    
    root2 = Tk()
    root2.title("Library")
    root2.minsize(width=400,height=400)
    root2.geometry("1200x700")


    Canvas1 = Canvas(root2) 
    Canvas1.config(bg="light sky blue")
    Canvas1.pack(expand=True,fill=BOTH)

    labelFrame = Frame(root2,bg='black')
    labelFrame.place(relx=0.01,rely=0.375,relwidth=0.96,relheight=0.515)
    sb = Scrollbar(labelFrame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    
    tree = ttk.Treeview(labelFrame, column=("c1", "c2", "c3", "c4","c5","c6","c7"), show='headings')
    style = ttk.Style(root2)
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
    tree.heading("#4", text="ISSUED TO")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="CLASS")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="SECTION")
    tree.column("#7", anchor=tk.CENTER)
    tree.heading("#7", text="DATE OF ISSUE")

    # Treeview Column Formate
    tree.column('#1', width=50, anchor=CENTER)
    tree.column('#2', width=250, anchor=W)
    tree.column('#3', width=125, anchor=W)
    tree.column('#4', width=120, anchor=CENTER)
    tree.column('#5', width=65, anchor=CENTER)
    tree.column('#6', width=90, anchor=CENTER)
    tree.column('#7', width=150, anchor=CENTER)
    tree.place(relx=0.01,rely=0.1,relwidth=0.96,relheight=0.8)

    tree.config(yscrollcommand=sb.set)
    sb.config(command=tree.yview)

    calanderimg = PhotoImage(file='Calendar.png',master = root2)
    calanderimg = calanderimg.subsample(1,1)

    clockimg = PhotoImage(file='Clock.png',master=root2)
    clockimg = clockimg.subsample(1,1)

    headingFrame1 = Frame(root2,bg="black", bd=5)
    headingFrame1.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.1)

    headingLabel = Label(headingFrame1, text="DAV LIBRARY", bg='light sea green', fg='midnight blue', font=('Courier',26,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    dateFrame = Frame(root2, bg="black", bd=3)
    dateFrame.place(relx=0.15,rely=0.18, relwidth=0.355, relheight=0.075)

    dateLabel = Label(dateFrame,image = calanderimg, font=('times', 14, 'bold'), bg='#E5EACA', compound ='left')
    dateLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    date_string = time.strftime("%d/%m/%Y")
    dateLabel.configure(text=" Date : " + date_string)

    timeFrame = Frame(root2, bg="black", bd=3)
    timeFrame.place(relx=0.525,rely=0.18, relwidth=0.325, relheight=0.075)

    clocktimLabel = Label(timeFrame,image = clockimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    clocktimLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    Date_Tim()
         
    headingFrame2 = Frame(root2,bg="#FFBB00",bd=5)
    headingFrame2.place(relx=0.25,rely=0.28,relwidth=0.5,relheight=0.08)
        
    headingLabel1 = Label(headingFrame2, text="View Issued Books", bg='black', fg='white', font=('Courier',26,'bold','italic'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)
    
        
    getBooks = "select "+bookTable+".bid, title, author, issuedto, class, section, dateofissue from "+bookTable+","+issueTable+" where "+bookTable+".bid = "+issueTable+".bid"
    try:
        con.commit()
        cur.execute(getBooks)
        rows = cur.fetchall()    
        for row in rows:
            rowlist = list(row)
            rowlist[6] = rowlist[6].strftime("%d-%m-%y")
            rownew = tuple(rowlist)
            tree.insert("", tk.END, values=rownew)        
    except:
        messagebox.showinfo("Notification","Failed to fetch files from database")

    fileBtn = Button(root2,text="EXCEL FILE",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=issuedFile)
    fileBtn.place(relx=0.25,rely=0.9, relwidth=0.18,relheight=0.08)        
    
    quitBtn = Button(root2,text="QUIT",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=root2.destroy)
    quitBtn.place(relx=0.55,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root2.mainloop()
#viewIssued()
