from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkfont
import mysql.connector as mysql
import datetime
import time

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = mysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "issue_history"
bookTable = "books"

def findissued():
    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.01,rely=0.5,relwidth=0.96,relheight=0.38)
    sb = Scrollbar(labelFrame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    
    tree = ttk.Treeview(labelFrame, column=("c1", "c2", "c3","c4", "c5", "c6", "c7","c8","c9"), show='headings')
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
    tree.heading("#4", text="ISSUED TO")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="CLASS")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="SECTION")
    tree.column("#7", anchor=tk.CENTER)
    tree.heading("#7", text="DATE OF ISSUE")
    tree.column("#8", anchor=tk.CENTER)
    tree.heading("#8", text="DATE OF RETURN")
    tree.column("#9", anchor=tk.CENTER)
    tree.heading("#9", text="FINE PAID")
    tree.place(relx=0.01,rely=0.1,relwidth=0.96,relheight=0.8)

    tree.config(yscrollcommand=sb.set)
    sb.config(command=tree.yview)

    # Treeview Column Formate
    tree.column('#1', width=35, anchor=CENTER)
    tree.column('#2', width=150, anchor=W)
    tree.column('#3', width=80, anchor=W)
    tree.column('#4', width=60, anchor=CENTER)
    tree.column('#5', width=35, anchor=CENTER)
    tree.column('#6', width=55, anchor=CENTER)
    tree.column('#7', width=100, anchor=CENTER)
    tree.column('#8', width=120, anchor=CENTER)
    tree.column('#9', width=55, anchor=CENTER)

    fromdate = bookInfo1.get_date()
    todate = bookInfo2.get_date()
    fromdate1 = fromdate.strftime("%Y-%m-%d")
    todate1 = todate.strftime("%Y-%m-%d") 
    getBooks = "select "+bookTable+".bid,title,author,issuedto,class,section,dateofissue,dateofreturn,fine from "+bookTable+","+issueTable+" where  "+bookTable+".bid = "+issueTable+".bid and dateofissue between '"+str(fromdate1)+"' and '"+str(todate1)+"'"
    try:
        con.commit()
        cur.execute(getBooks)
        rows = cur.fetchall()
        i = 0
        for row in rows:
            i = i+1
            rowlist = list(row)
            rowlist[6] = rowlist[6].strftime("%d-%m-%y")
            if rowlist[7] == None:
                rowlist[7] = "Not Returned"
            else:
                rowlist[7] = rowlist[7].strftime("%d-%m-%y")
            if rowlist[8] == None:
                rowlist[8] = 0
            rownew = tuple(rowlist)
            tree.insert("", tk.END, values=rownew)
        if i == 0:
            messagebox.showinfo("Search Result","There are no issued books between the given dates")            
        
    except:
        messagebox.showinfo("Notification","Failed to fetch details from database")
    
    
def searchissued():

    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
    
    global root1, bookInfo1, bookInfo2
    
    root1 = Tk()
    root1.title("Library")
    root1.minsize(width=400,height=400)
    root1.geometry("1300x600")


    Canvas1 = Canvas(root1) 
    Canvas1.config(bg="aquamarine2")
    Canvas1.pack(expand=True,fill=BOTH)

    calanderimg = PhotoImage(file='Calendar.png',master=root1)
    calanderimg = calanderimg.subsample(1,1)

    clockimg = PhotoImage(file='Clock.png',master=root1)
    clockimg = clockimg.subsample(1,1)

    headingFrame1 = Frame(root1,bg="black", bd=5)
    headingFrame1.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.1)

    headingLabel = Label(headingFrame1, text="DAV LIBRARY", bg='light sea green', fg='midnight blue', font=('Courier',26,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    dateFrame = Frame(root1, bg="black", bd=3)
    dateFrame.place(relx=0.15,rely=0.18, relwidth=0.355, relheight=0.075)

    dateLabel = Label(dateFrame,image = calanderimg, font=('times', 14, 'bold'), bg='#E5EACA', compound ='left')
    dateLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    date_string = time.strftime("%d/%m/%Y")
    dateLabel.configure(text=" Date : " + date_string)

    timeFrame = Frame(root1, bg="black", bd=3)
    timeFrame.place(relx=0.525,rely=0.18, relwidth=0.325, relheight=0.075)

    clocktimLabel = Label(timeFrame,image = clockimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    clocktimLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    Date_Tim()


    headingFrame2 = Frame(root1,bg="#FFBB00",bd=5)
    headingFrame2.place(relx=0.2,rely=0.28,relwidth=0.6,relheight=0.08)
        
    headingLabel1 = Label(headingFrame2, text="Search by Date of Issue", bg='black', fg='white', font=('Courier',24,'bold'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.1,rely=0.38,relwidth=0.8,relheight=0.1)   
        
    # Book ID to be searched
    lb1 = Label(labelFrame,text="FROM DATE: ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb1.place(relx=0.05,rely=0.25)
        
    bookInfo1 = DateEntry(labelFrame,selectmode='day')
    bookInfo1.place(relx=0.25,rely=0.25)
    bookInfo1.bind("<Key>", lambda e: "break")

    lb2 = Label(labelFrame,text="TO DATE: ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb2.place(relx=0.55,rely=0.25)
        
    bookInfo2 = DateEntry(labelFrame,selectmode='day')
    bookInfo2.place(relx=0.75,rely=0.25)
    bookInfo2.bind("<Key>", lambda e: "break")
        
    #Submit Button
    SubmitBtn = Button(root1,text="SEARCH",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=findissued)
    SubmitBtn.place(relx=0.25,rely=0.9, relwidth=0.18,relheight=0.08)
      
    quitBtn = Button(root1,text="QUIT",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=root1.destroy)
    quitBtn.place(relx=0.55,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root1.mainloop()

#searchissued()

    

    
