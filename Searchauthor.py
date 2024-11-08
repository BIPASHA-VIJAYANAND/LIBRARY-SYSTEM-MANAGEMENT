from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkfont
import mysql.connector as mysql
import time

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = mysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"

def findauthor():
    author = bookInfo1.get()
    if len(author) == 0:
        messagebox.showinfo("Notification","Please provide valid input for Author")
    else:        
        labelFrame1 = Frame(root3,bg='black')
        labelFrame1.place(relx=0.01,rely=0.52,relwidth=0.96,relheight=0.35)
        sb = Scrollbar(labelFrame1, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(labelFrame1, column=("c1", "c2", "c3", "c4"), show='headings')
        style = ttk.Style(root3)
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
        tree.place(relx=0.01,rely=0.1,relwidth=0.96,relheight=0.8)

        tree.config(yscrollcommand=sb.set)
        sb.config(command=tree.yview)

        getBooks = "select * from "+bookTable+" where author like '%"+author+"%'"
        try:
            con.commit()
            cur.execute(getBooks)
            rows = cur.fetchall()
            i = 0
            for row in rows:
                i = i+1
                tree.insert("", tk.END, values=row)
            if i == 0:
                messagebox.showinfo("Search Result","Author is not present")            
        
        except:
            messagebox.showinfo("Notification","Failed to fetch details from database")
    
    
def searchAuthor():
    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
    
    global root3, bookInfo1
    
    root3 = Tk()
    root3.title("Library")
    root3.minsize(width=400,height=400)
    root3.geometry("872x700")


    Canvas1 = Canvas(root3) 
    Canvas1.config(bg="LightGoldenrod1")
    Canvas1.pack(expand=True,fill=BOTH)
    
    calanderimg = PhotoImage(file='Calendar.png',master=root3)
    calanderimg = calanderimg.subsample(1,1)

    clockimg = PhotoImage(file='Clock.png',master=root3)
    clockimg = clockimg.subsample(1,1)

    headingFrame1 = Frame(root3,bg="black", bd=5)
    headingFrame1.place(relx=0.05,rely=0.05,relwidth=0.8,relheight=0.1)

    headingLabel = Label(headingFrame1, text="DAV LIBRARY", bg='light sea green', fg='midnight blue', font=('Courier',26,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    dateFrame = Frame(root3, bg="black", bd=3)
    dateFrame.place(relx=0.1,rely=0.19, relwidth=0.355, relheight=0.075)

    dateLabel = Label(dateFrame,image = calanderimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    dateLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    date_string = time.strftime("%d/%m/%Y")
    dateLabel.configure(text=" Date : " + date_string)

    timeFrame = Frame(root3, bg="black", bd=3)
    timeFrame.place(relx=0.475,rely=0.19, relwidth=0.325, relheight=0.075)

    clocktimLabel = Label(timeFrame,image = clockimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    clocktimLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    Date_Tim()

    headingFrame2 = Frame(root3,bg="#FFBB00",bd=5)
    headingFrame2.place(relx=0.25,rely=0.29,relwidth=0.5,relheight=0.1)
        
    headingLabel1 = Label(headingFrame2, text="Search by Author", bg='black', fg='white', font=('Courier',26,'bold'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root3,bg='black')
    labelFrame.place(relx=0.075,rely=0.42,relwidth=0.8,relheight=0.075)   
        
    # Author to be searched
    lb1 = Label(labelFrame,text="Author : ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb1.place(relx=0.05,rely=0.3)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.3, relwidth=0.5)
        
    #Submit Button
    SubmitBtn = Button(root3,text="SEARCH",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=findauthor)
    SubmitBtn.place(relx=0.25,rely=0.9, relwidth=0.18,relheight=0.08)
      
    quitBtn = Button(root3,text="QUIT",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=root3.destroy)
    quitBtn.place(relx=0.55,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root3.mainloop()

#searchAuthor()

    

    
