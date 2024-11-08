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
issueTable = "books_issued" 
bookTable = "books" #Book Table

allBid = [] #List To store all Book IDs

def deleteBook():
    
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
    
        if status==True:
            getdetails = "select * from "+bookTable+" where bid="+bid
            try:
                cur.execute(getdetails)
                for i in cur:
                    title = i[1]
                    author = i[2]
            except:
                messagebox.showinfo("Notification","Can't fetch the given Book ID")
                root.destroy()
                return
            title = title.upper()
            author = author.upper()
            delMsg = "Do You Really Want To Delete The Book with Id "+bid+"\n Titled '"+title+"' and Author '"+author+"'  !!!!!"
            delCon = messagebox.askyesno("CONFIRM", delMsg,parent = root)
            if delCon == True:
                deleteSql = "delete from "+bookTable+" where bid="+bid
                deleteIssue = "delete from "+issueTable+" where bid="+bid
                try:
                    cur.execute(deleteSql)
                    con.commit()
                    cur.execute(deleteIssue)
                    con.commit()
                    messagebox.showinfo('Success',"Book Record Deleted Successfully")
                except:
                    messagebox.showinfo('Notification',"Please check Book ID")
 

                bookInfo1.delete(0, END)
                root.destroy()
            elif delCon == False:
                bookInfo1.delete(0, END)
                return
        else:
            messagebox.showinfo("Notification","Book ID not present")
            root.destroy()
            return
    
def delete():

    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
        
    global bookInfo1,Canvas1,con,cur,bookTable,root
    
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
        
    headingLabel1 = Label(headingFrame2, text="Delete Book", bg='black', fg='white', font=('Courier',26,'bold','italic'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.075,rely=0.49,relwidth=0.75,relheight=0.25)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID: ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb2.place(relx=0.05,rely=0.4)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.35,rely=0.4, relwidth=0.5)
    
    #Submit Button
    SubmitBtn = Button(root,text="DELETE",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.8, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.8, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
#delete()
