from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as mysql
from tkinter import ttk
import datetime as dt
import time

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = mysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued"
issuehistory = "issue_history"
bookTable = "books"
    
#List To store all Book IDs
allBid = [] 

    
def issueBook():
    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)

    def issue():
    
        bid = inf1.get()
        issueto = inf2.get()
        studclass = inf3.get()
        sect = inf4.get()
        date=dt.datetime.now()

        if len(bid) == 0 and len(issueto) == 0 and len(studclass) == 0 and len(sect) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Book id, Issued to, Students Class & Section")
        elif len(bid) == 0 and len(issueto) == 0 and len(studclass) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Book id, Issued to & Students Class")
        elif len(bid) == 0 and len(issueto) == 0 and len(sect) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Book id, Issued to & Section")
        elif len(bid) == 0 and len(studclass) == 0 and len(sect) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Book id, Students class & Section")
        elif len(issueto) == 0 and len(studclass) == 0 and len(sect) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Issued to, Students class & Section")
        elif len(issueto) == 0 and len(sect) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Issued to & Section")
        elif len(issueto) == 0 and len(studclass) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Issued to & Students class")
        elif len(bid) == 0 and len(issueto) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Book id & Issued to")
        elif len(bid) == 0 and len(studclass) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Book id & Students class")
        elif len(bid) == 0 and len(sect) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Book id & Section")
        elif len(studclass) == 0 and len(sect) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Students class & Section")
        elif len(bid) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Book ID")
        elif len(issueto) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Issued to")
        elif len(studclass) == 0:
            messagebox.showinfo("Notification","Please provide valid input for Students class")
        elif len(sect) == 0:
            messagebox.showinfo("Notification","Please provide valid input for section")
        elif studclass.upper() not in ("I", "II", "III", "IV","V","VI","VII","VIII","IX","X","XI","XII"):
            messagebox.showinfo("Notification","Please provide valid input for Students class")
        elif sect.upper() not in ("A", "B", "C"):
            messagebox.showinfo("Notification","Please provide valid input for section")
        else:
            extractBid = "select bid from "+bookTable
            try:
                cur.execute(extractBid)
        
                for i in cur:
                    allBid.append(i[0])
        
                if int(bid) in allBid:
            
                    checkAvail = "select status from "+bookTable+" where bid="+bid
                    cur.execute(checkAvail)
            
                    for i in cur:
                        check = i[0]
                
                    if check == 'avail':
                        status = True
                    else:
                        status = False

                else:
                    messagebox.showinfo("Notification","Book ID not present")
                    issueroot.destroy()
                    return
            except:
                messagebox.showinfo("Notification","Can't fetch Book IDs")
    
            issueSql = "insert into "+issueTable+" values ("+bid+",'"+issueto+"','"+studclass+"','"+sect+"','"+str(date)+"')"
            historySql = "insert into "+issuehistory+"(bid,issuedto,class,section,dateofissue) values ("+bid+",'"+issueto+"','"+studclass+"','"+sect+"','"+str(date)+"')"
            updateStatus = "update "+bookTable+" set status = 'issued' where bid = "+bid
            try:
                if int(bid) in allBid and status == True:
                    cur.execute(issueSql)
                    con.commit()
                    cur.execute(historySql)
                    con.commit()
                    cur.execute(updateStatus)
                    con.commit()
                    messagebox.showinfo('Success',"Book Issued Successfully")
                    issueroot.destroy()
                else:
                    allBid.clear()
                    messagebox.showinfo('Notification',"Book Already Issued")
                    issueroot.destroy()
                    return
            except:
                messagebox.showinfo("Notification","The value entered is wrong, Try again")
   
    
        allBid.clear()

    
    global inf1, inf2, inf3, inf4, issueroot, Canvas1, status
    
    issueroot = Tk()
    issueroot.title("Library")
    issueroot.minsize(width=400,height=400)
    issueroot.geometry("600x500")
    
    Canvas1 = Canvas(issueroot)
    Canvas1.config(bg="khaki1")
    Canvas1.pack(expand=True,fill=BOTH)

    calanderimg = PhotoImage(file='Calendar.png', master=issueroot)
    calanderimg = calanderimg.subsample(1,1)

    clockimg = PhotoImage(file='Clock.png', master=issueroot)
    clockimg = clockimg.subsample(1,1)

    headingFrame1 = Frame(issueroot,bg="black", bd=5)
    headingFrame1.place(relx=0.05,rely=0.05,relwidth=0.8,relheight=0.1)

    headingLabel = Label(headingFrame1, text="DAV LIBRARY", bg='light sea green', fg='midnight blue', font=('Courier',26,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    dateFrame = Frame(issueroot, bg="black", bd=3)
    dateFrame.place(relx=0.1,rely=0.19, relwidth=0.355, relheight=0.075)

    dateLabel = Label(dateFrame,image = calanderimg, font=('times', 14, 'bold'), bg='#E5EACA', compound ='left')
    dateLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    date_string = time.strftime("%d/%m/%Y")
    dateLabel.configure(text=" Date : " + date_string)

    timeFrame = Frame(issueroot, bg="black", bd=3)
    timeFrame.place(relx=0.475,rely=0.19, relwidth=0.325, relheight=0.075)

    clocktimLabel = Label(timeFrame,image = clockimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    clocktimLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    Date_Tim()

    headingFrame2 = Frame(issueroot,bg="#FFBB00",bd=5)
    headingFrame2.place(relx=0.225,rely=0.29,relwidth=0.5,relheight=0.1)
        
    headingLabel1 = Label(headingFrame2, text="Issue Book", bg='black', fg='white', font=('Courier',26,'bold','italic'))
    headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(issueroot,bg='black')
    labelFrame.place(relx=0.05,rely=0.45,relwidth=0.8,relheight=0.3)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb1.place(relx=0.05,rely=0.1)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.35,rely=0.1, relwidth=0.5)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb2.place(relx=0.05,rely=0.3)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.35,rely=0.3, relwidth=0.5)

    lb3 = Label(labelFrame,text="Class : ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb3.place(relx=0.05,rely=0.5)
    
    inf3 = ttk.Combobox(labelFrame, values=["I", "II", "III", "IV","V","VI","VII","VIII","IX","X","XI","XII"])
    inf3.place(relx=0.35,rely=0.5, relwidth=0.5)

    lb4 = Label(labelFrame,text="Section : ", bg='black', fg='white', font=('Courier',15,'bold'))
    lb4.place(relx=0.05,rely=0.7)

    inf4 = ttk.Combobox(labelFrame, values=["A", "B", "C"])
    inf4.place(relx=0.35,rely=0.7, relwidth=0.07)

    
    #Issue Button
    issueBtn = Button(issueroot,text="ISSUE",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(issueroot,text="QUIT",bg='#f7f1e3', fg='black', font=('Courier',15,'bold'), command=issueroot.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    issueroot.mainloop()
#issueBook()
