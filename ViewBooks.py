from tkinter import *
from PIL import ImageTk,Image
import time
from ViewAllBooks import *
from ViewIssued import *
from ViewDefaulters import *


def quitpg():
    root.destroy()

def viewmainpg():
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

    dateFrame = Frame(root, bg="black", bd=3)
    dateFrame.place(relx=0.1,rely=0.19, relwidth=0.355, relheight=0.075)

    dateLabel = Label(dateFrame,image = calanderimg, font=('times', 14, 'bold'), bg='#E5EACA', compound ='left')
    dateLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    date_string = time.strftime("%d/%m/%Y")
    dateLabel.configure(text=" Date : " + date_string)

    timeFrame = Frame(root, bg="black", bd=3)
    timeFrame.place(relx=0.475,rely=0.19, relwidth=0.325, relheight=0.075)

    clocktimLabel = Label(timeFrame,image = clockimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    clocktimLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    Date_Tim()
        
    headingFrame2 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame2.place(relx=0.2,rely=0.29,relwidth=0.5,relheight=0.1)
        
    headingLabel1 = Label(headingFrame2, text="View Books", bg='black', fg='white', font=('Courier',26,'bold','italic'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="View All books",bg='pale green', fg='saddle brown',font=('Courier',15,'bold'), command=viewall)
    btn1.place(relx=0.2,rely=0.42, relwidth=0.5,relheight=0.1)
    
    btn2 = Button(root,text="View All Issued Books",bg='pale green', fg='saddle brown', font=('Courier',15,'bold'), command=viewIssued)
    btn2.place(relx=0.2,rely=0.54, relwidth=0.5,relheight=0.1)

    btn3 = Button(root,text="View Defaulters",bg='pale green', fg='saddle brown', font=('Courier',15,'bold'), command=defaultersView)
    btn3.place(relx=0.2,rely=0.66, relwidth=0.5,relheight=0.1)

    quitBtn = Button(root,text="Quit View",bg='pale green', fg='saddle brown', font=('Courier',15,'bold'), command=quitpg)
    quitBtn.place(relx=0.2,rely=0.78, relwidth=0.5,relheight=0.1)
	
    root.mainloop()
#viewmainpg()
    
