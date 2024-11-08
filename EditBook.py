from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as mysql
import time


# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = mysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" #Book Table

allBid = [] #List To store all Book IDs

def editcheck():
    bid = bookInfo1.get()
    if len(bid) == 0:
        messagebox.showinfo("Notification","Please provide valid input for Book ID")
    else:        
        extractBid = "select bid from "+bookTable
        try:
            cur.execute(extractBid)
        
            for i in cur:
                allBid.append(i[0])

            if int(bid) in allBid:
                status = True
            else:
                status = False
        except:
            messagebox.showinfo("Notification","Can't fetch the given Book ID")
            root.destroy()
            return
        
        if status == True:
            editbookInfo1.insert(0,bid)
            getBook = "select * from "+bookTable+" where bid = "+bid
            try:
                cur.execute(getBook)
                data = cur.fetchall()    
                for i in data:
                    editbookInfo2.insert(0,i[1])
                    editbookInfo3.insert(0,i[2])
            except:
                messagebox.showinfo("Notification","Failed to fetch book from database")
            labelFrame.place_forget()
            labelFrame2.place(relx=0.05,rely=0.45,relwidth=0.8,relheight=0.25)
            editbookInfo1.configure(state = 'disable')
            SubmitBtn.place_forget()
            SubmitBtn1.place(relx=0.28,rely=0.8, relwidth=0.18,relheight=0.08)
            return
        elif status == False:
            messagebox.showinfo("Notification","There is no such book with the given book id!!!")
            root.destroy()
            return

def editBook():
    bid = editbookInfo1.get()
    title = editbookInfo2.get()
    author = editbookInfo3.get()
    if len(title) == 0 and len(author) == 0:
        messagebox.showinfo("Notification","Please provide valid input for Title & Author")
    elif len(title) == 0:
        messagebox.showinfo("Notification","Please provide valid input for Title")
    elif len(author) == 0:
        messagebox.showinfo("Notification","Please provide valid input for Author")
    else:
        editMsg = "Do You Really Want To Edit The Book with Id "+bid+" ?"
        editCon = messagebox.askyesno("CONFIRM", editMsg,parent = root)
        if editCon == True:
            title=title.title()
            author=author.title()
            editbk = "update "+bookTable+" set title = '"+title+"', author = '"+author+"' where bid = "+bid
            try:
                cur.execute(editbk)
                con.commit()
                messagebox.showinfo('Success',"Book edited successfully")
            except:
                messagebox.showinfo("Notification","Can't edit data in Database")
        elif editCon == False:
            return
        root.destroy()
    return          
    
def editmain():

    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
        
    global bid,bookInfo1,Canvas1,con,cur,bookTable,root,lb1,labelFrame,labelFrame2,bookInfo1,editbookInfo1,editbookInfo2,editbookInfo3,editlb1,editlb2,editlb3,idvalue,titlename,authorname,SubmitBtn,SubmitBtn1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="light green")
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
    headingFrame2.place(relx=0.225,rely=0.29,relwidth=0.5,relheight=0.13)
        
    headingLabel1 = Label(headingFrame2, text="Edit Book", bg='black', fg='white', font=('Courier',26,'bold','italic'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.075,rely=0.49,relwidth=0.75,relheight=0.25)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID: ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb1.place(relx=0.05,rely=0.4)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.35,rely=0.4, relwidth=0.5)

    labelFrame2 = Frame(root,bg='black')
    labelFrame2.place_forget()

    idvalue = StringVar()
    titlename = StringVar()
    authorname = StringVar()

    # Book Id
    editlb1 = Label(labelFrame2,text="BookId : ", bg='black', fg='white', font=('Courier',15,'bold'),)
    editlb1.place(relx=0.05,rely=0.2, relheight=0.175)

    editbookInfo1 = Entry(labelFrame2, textvariable=idvalue)
    editbookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.175)
        
    # Title
    editlb2 = Label(labelFrame2,text="Title : ", bg='black', fg='white', font=('Courier',15,'bold'))
    editlb2.place(relx=0.05,rely=0.4, relheight=0.175)
        
    editbookInfo2 = Entry(labelFrame2, textvariable=titlename)
    editbookInfo2.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.175)
        
    # Book Author
    editlb3 = Label(labelFrame2,text="Author : ", bg='black', fg='white', font=('Courier',15,'bold'))
    editlb3.place(relx=0.05,rely=0.6, relheight=0.175)
        
    editbookInfo3 = Entry(labelFrame2, textvariable=authorname)
    editbookInfo3.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.175)
    
    #Submit Button
    SubmitBtn = Button(root,text="EDIT",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=editcheck)
    SubmitBtn.place(relx=0.28,rely=0.8, relwidth=0.18,relheight=0.08)

    SubmitBtn1 = Button(root,text="SAVE",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=editBook)
    SubmitBtn1.place_forget()
    
    quitBtn = Button(root,text="QUIT",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.8, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
#editmain()
