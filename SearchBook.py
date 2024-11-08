from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkfont
from Searchbid import *
from Searchauthor import *
from Searchissued import *
import time

def quitpg():
    root.destroy()

def searchBook():
    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
    
    global root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="PaleVioletRed1")
    Canvas1.pack(expand=True,fill=BOTH)

    calanderimg = PhotoImage(file='Calendar.png', master=root)
    calanderimg = calanderimg.subsample(1,1)

    clockimg = PhotoImage(file='Clock.png', master=root)
    clockimg = clockimg.subsample(1,1)

    headingFrame1 = Frame(root,bg="black", bd=5)
    headingFrame1.place(relx=0.05,rely=0.05,relwidth=0.8,relheight=0.1)

    headingLabel = Label(headingFrame1, text="DAV LIBRARY", bg='light sea green', fg='midnight blue', font=('Courier',26,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    dateFrame1 = Frame(root, bg="black", bd=3)
    dateFrame1.place(relx=0.1,rely=0.19, relwidth=0.355, relheight=0.075)

    dateLabel = Label(dateFrame1,image = calanderimg, font=('times', 14, 'bold'), bg='#E5EACA', compound ='left')
    dateLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    date_string = time.strftime("%d/%m/%Y")
    dateLabel.configure(text=" Date : " + date_string)

    timeFrame1 = Frame(root, bg="black", bd=3)
    timeFrame1.place(relx=0.475,rely=0.19, relwidth=0.325, relheight=0.075)

    clocktimLabel = Label(timeFrame1,image = clockimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    clocktimLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    Date_Tim()
        
    headingFrame2 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame2.place(relx=0.2,rely=0.29,relwidth=0.5,relheight=0.1)
        
    headingLabel1 = Label(headingFrame2, text="Search Book", bg='black', fg='white', font=('Courier',26,'bold','italic'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Search by Book ID",bg='pale green', fg='saddle brown',font=('Courier',15,'bold'), command=searchBid)
    btn1.place(relx=0.2,rely=0.42, relwidth=0.5,relheight=0.1)
    
    btn2 = Button(root,text="Search by Book Author",bg='pale green', fg='saddle brown', font=('Courier',15,'bold'), command=searchAuthor)
    btn2.place(relx=0.2,rely=0.54, relwidth=0.5,relheight=0.1)

    btn3 = Button(root,text="Search by Date of Issue",bg='pale green', fg='saddle brown', font=('Courier',15,'bold'), command=searchissued)
    btn3.place(relx=0.2,rely=0.66, relwidth=0.5,relheight=0.1)

    quitBtn = Button(root,text="Quit Search",bg='pale green', fg='saddle brown', font=('Courier',15,'bold'), command=quitpg)
    quitBtn.place(relx=0.2,rely=0.78, relwidth=0.5,relheight=0.1)
	
    root.mainloop()
#searchBook()
    
