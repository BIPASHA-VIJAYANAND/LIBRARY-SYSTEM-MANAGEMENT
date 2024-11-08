from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as mysql
import datetime as dt
import time

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = mysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" #Issue Table
issuehistory = "issue_history"
bookTable = "books" #Book Table


allBid = [] #List To store all Book IDs

def returnn():

    bid = bookInfo1.get()
    date=dt.datetime.now()
    visit = 0
    
    if len(bid) == 0:
        messagebox.showinfo("Notification","Please provide valid input for Book ID")
    else:        
        extractBid = "select bid from "+issueTable
        try:
            cur.execute(extractBid)
        
            for i in cur:
                allBid.append(i[0])
            
            
            if int(bid) in allBid:
            
                checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
                cur.execute(checkAvail)
            
                for i in cur:
                    check = i[0]
                
                if check == 'issued':
                    status = True
                else:
                    status = False

            else:
                messagebox.showinfo("Notification","Book with this book id isn't issued!!!")
                root.destroy()
                return
        except:
            messagebox.showinfo("Notification","Given Book ID is not present")
            root.destroy()
            return
    
        issueSql = "delete from "+issueTable+" where bid = "+bid
        dateSql = "select dateofissue from "+issueTable+" where bid = "+bid
        updateStatus = "update "+bookTable+" set status = 'avail' where bid = "+bid
        try:
            if int(bid) in allBid and status == True:
                cur.execute(dateSql)
            
                for i in cur:
                    issueddate = i[0]
                
                delta = date - issueddate
                days = delta.days
                updatehistory = "update "+issuehistory+" set dateofreturn = '"+str(date)+"' where bid = "+bid+" and dateofissue = '"+str(issueddate)+"'"     
                if days <= 7:
                    updatefine = "update "+issuehistory+" set fine = 0 where bid = "+bid
                    cur.execute(issueSql)
                    con.commit()
                    cur.execute(updateStatus)
                    con.commit()
                    cur.execute(updatefine)
                    con.commit()
                    cur.execute(updatehistory)
                    con.commit()
                    messagebox.showinfo('Success',"Book Returned Successfully")
                    visit = 1
                else:
                    fineroot = Tk()
                    fineroot.title('Late Fine')
                    fineroot.geometry('250x250')
                    fineroot.resizable(False, False)

                    fineframe = Frame(fineroot, bd=5, relief='groove', bg='powder blue')
                    fineframe.place(x=0, y=0, relwidth=1, relheight=1)

                    Duedatelabel = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue',text='Issued Date : ')
                    Duedatelabel.place(x=20, y=20)

                    Duedatelabelval = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue', text=issueddate.strftime("%d-%m-%y"), fg='red')
                    Duedatelabelval.place(x=120, y=20)

                    Todaydatelabel = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue', text='Today Date : ')
                    Todaydatelabel.place(x=20, y=70)

                    Todaydatelabelval = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue',text=time.strftime("%d-%m-%y"), fg='red')
                    Todaydatelabelval.place(x=120, y=70)

                    finedatelabel = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue', text='Late Fine : ')
                    finedatelabel.place(x=20, y=120)

                    fine = (days-7)*5
                    finedatelabelval = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue', text=fine, fg='red')
                    finedatelabelval.place(x=120, y=120)
                    updatefine = "update "+issuehistory+" set fine = "+str(fine)+" where bid = "+bid

                    def FinePaidfun():
                        try:
                            cur.execute(issueSql)
                            con.commit()
                            cur.execute(updateStatus)
                            con.commit()
                            cur.execute(updatehistory)
                            con.commit()
                            cur.execute(updatefine)
                            con.commit()
                            messagebox.showinfo('Success',"Book Returned Successfully")
                            fineroot.destroy()
                            root.destroy()
                            return
                        except:
                            messagebox.showinfo("Notification","Couldn't return the Book!!!")
                            fineroot.destroy()
                            root.destroy()
                            return
                            
                    finebutton = Button(fineframe, text='Paid', font=("Arial", 12, "bold"), bd=5, bg='blue', fg='white', command=FinePaidfun)
                    finebutton.place(x=150, y=190)
                    
            else:
                allBid.clear()
                messagebox.showinfo('Notification',"Please check the book ID")
                root.destroy()
                return
        except:
            messagebox.showinfo("Notification","The value entered is wrong, Try again")
            visit = 1
    
    
        allBid.clear()
        if visit == 1:
            root.destroy()
    
def returnBook():
    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
    
    global bookInfo1,Canvas1,con,cur,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="plum1")
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
    headingFrame2.place(relx=0.2,rely=0.29,relwidth=0.5,relheight=0.13)
        
    headingLabel1 = Label(headingFrame2, text="Return Book", bg='black', fg='white', font=('Courier',26,'bold','italic'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.075,rely=0.49,relwidth=0.75,relheight=0.25)   
        
    # Book ID to Return
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb1.place(relx=0.05,rely=0.3)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.35,rely=0.3, relwidth=0.5, relheight=0.25)
    
    #Submit Button
    SubmitBtn = Button(root,text="RETURN",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=returnn)
    SubmitBtn.place(relx=0.2,rely=0.85, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=root.destroy)
    quitBtn.place(relx=0.5,rely=0.85, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
#returnBook()
