from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as mysql
import time

def bookRegister():
    
    title = bookInfo2.get()
    author = bookInfo3.get()
    

    if len(title) == 0 and len(author) == 0:
        messagebox.showinfo("Notification","Please provide valid input for Title & Author")
    elif len(title) == 0:
        messagebox.showinfo("Notification","Please provide valid input for Title")
    elif len(author) == 0:
        messagebox.showinfo("Notification","Please provide valid input for Author")
    else:
        title=title.title()
        author=author.title()
        status='avail'
        insertBooks = "insert into "+bookTable+"(title,author,status) values('"+title+"','"+author+"','"+status+"')"
        try:
            cur.execute(insertBooks)
            con.commit()
            messagebox.showinfo('Success',"Book added successfully")
        except:
            messagebox.showinfo("Notification","Can't add data into Database")
        root.destroy()
    
def addBook():

    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
    
    global bookInfo2,bookInfo3,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("550x500")

    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase="db"

    con = mysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="light pink")
    Canvas1.pack(expand=True,fill=BOTH)

    calanderimg = PhotoImage(file='Calendar.png',master=root)
    calanderimg = calanderimg.subsample(1,1)

    clockimg = PhotoImage(file='Clock.png',master=root)
    clockimg = clockimg.subsample(1,1)

    headingFrame1 = Frame(root,bg="black", bd=5)
    headingFrame1.place(relx=0.05,rely=0.05,relwidth=0.8,relheight=0.1)

    headingLabel = Label(headingFrame1, text="DAV LIBRARY", bg='light sea green', fg='midnight blue', font=('Courier',26,'bold','italic'))
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
    headingFrame2.place(relx=0.25,rely=0.32,relwidth=0.5,relheight=0.1)

    headingLabel1 = Label(headingFrame2, text="Add Book", bg='black', fg='white', font=('Courier',26,'bold'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.05,rely=0.45,relwidth=0.8,relheight=0.25)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb2.place(relx=0.05,rely=0.2, relheight=0.175)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.175)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb3.place(relx=0.05,rely=0.6, relheight=0.175)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.175)

    
    #Submit Button
    SubmitBtn = Button(root,text="ADD",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.8, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#f7f1e3', fg='black',  font=('Courier',15,'bold'), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.8, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
#addBook()
