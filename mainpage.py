from tkinter import *
from PIL import ImageTk,Image
import time
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from SearchBook import *
from EditBook import *

def quitlogin():
        rootmain.destroy()
        
def mainpage():

    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)
    
    global rootmain
    rootmain = Tk()
    rootmain.title("Library")
    rootmain.minsize(width=400,height=400)
    rootmain.geometry("600x500")

    # Take n greater than 0.25 and less than 5
    same=True
    n=2.4

    # Adding a background image
    background_image =Image.open("bkg.png")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
    
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.LANCZOS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(rootmain)

    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    calanderimg = PhotoImage(file='Calendar.png',master=rootmain)
    calanderimg = calanderimg.subsample(1,1)

    clockimg = PhotoImage(file='Clock.png',master=rootmain)
    clockimg = clockimg.subsample(1,1)

    addbookimg = PhotoImage(file='addbookicon1.png',master=rootmain)
    addbookimg = addbookimg.subsample(6, 6)

    issuebookimg = PhotoImage(file='issuebookicon1.png',master=rootmain)
    issuebookimg = issuebookimg.subsample(13, 12)

    editbookimg = PhotoImage(file='editbookicon.png',master=rootmain)
    editbookimg = editbookimg.subsample(6, 6)

    returnbookimg = PhotoImage(file='returnbookicon.png',master=rootmain)
    returnbookimg = returnbookimg.subsample(3, 3)

    deletebookimg = PhotoImage(file='deletebookicon.png',master=rootmain)
    deletebookimg = deletebookimg.subsample(7, 7)

    showbookimg = PhotoImage(file='showbookicon1.png',master=rootmain)
    showbookimg = showbookimg.subsample(1,1)

    searchbookimg = PhotoImage(file='searchicon.png',master=rootmain)
    searchbookimg = searchbookimg.subsample(13, 13)

    logoutimg = PhotoImage(file='logouticon.png',master=rootmain)
    logoutimg = logoutimg.subsample(1,1)

    headingFrame1 = Frame(rootmain,bg="black", bd=5)
    headingFrame1.place(relx=0.05,rely=0.05,relwidth=0.8,relheight=0.1)

    headingLabel = Label(headingFrame1, text="DAV LIBRARY", bg='light sea green', fg='midnight blue', font=('Courier',26,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    dateFrame = Frame(rootmain, bg="black", bd=3)
    dateFrame.place(relx=0.1,rely=0.2, relwidth=0.325, relheight=0.075)

    dateLabel = Label(dateFrame,image = calanderimg, font=('times', 14, 'bold'), bg='#E5EACA', compound ='left')
    dateLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    date_string = time.strftime("%d/%m/%Y")
    dateLabel.configure(text=" Date : " + date_string)

    timeFrame = Frame(rootmain, bg="black", bd=3)
    timeFrame.place(relx=0.475,rely=0.2, relwidth=0.325, relheight=0.075)

    clocktimLabel = Label(timeFrame,image = clockimg, font=('times', 14, 'bold'), bg='#E5EACA',compound ='left')
    clocktimLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    Date_Tim()

    btn1 = Button(rootmain,text="Add Book", font=("Arial", 12, "bold italic"), fg='white', bg="#B07138", activebackground='red', activeforeground='white', bd=10, width=150, height=40, image=addbookimg, compound='left', command=addBook)
    btn1.place(relx=0.125,rely=0.35, relwidth=0.275,relheight=0.12)
    
    btn2 = Button(rootmain, text="Delete Book", font=("Arial", 12, "bold italic"), fg='white', bg="#B07138", activebackground='red', activeforeground='white', bd=10, width=150, height=40, image=deletebookimg, compound='left', command=delete)
    btn2.place(relx=0.5,rely=0.35, relwidth=0.275,relheight=0.12)
    
    btn3 = Button(rootmain,text="Issue Book", font=("Arial", 12, "bold italic"), fg='white', bg="#B07138", activebackground='red', activeforeground='white', bd=10, width=150, height=40, image=issuebookimg, compound='left', command = issueBook)
    btn3.place(relx=0.125,rely=0.5, relwidth=0.275,relheight=0.12)
    
    btn4 = Button(rootmain, text="Return Book", font=("Arial", 12, "bold italic"), fg='white', bg="#B07138", activebackground='red', activeforeground='white', bd=10, width=150, height=40, image=returnbookimg, compound='left', command = returnBook)
    btn4.place(relx=0.5,rely=0.5, relwidth=0.275,relheight=0.12)

    btn5 = Button(rootmain, text="Edit Book", font=("Arial", 12, "bold italic"), fg='white', bg="#B07138", activebackground='red', activeforeground='white', bd=10, width=150, height=40, image=editbookimg, compound='left', command = editmain)
    btn5.place(relx=0.125,rely=0.65, relwidth=0.275,relheight=0.12)

    btn6 = Button(rootmain, text="Show Book", font=("Arial", 12, "bold italic"), fg='white', bg="#B07138", activebackground='red', activeforeground='white', bd=10, width=150, height=40, image=showbookimg, compound='left', command=viewmainpg)
    btn6.place(relx=0.5,rely=0.65, relwidth=0.275,relheight=0.12)

    btn7 = Button(rootmain, text="Search Book", font=("Arial", 12, "bold italic"), fg='white', bg="#B07138", activebackground='red', activeforeground='white', bd=10, width=150, height=40, image=searchbookimg, compound='left', command = searchBook)
    btn7.place(relx=0.125,rely=0.8, relwidth=0.275,relheight=0.12)

    btn8 = Button(rootmain, text="  Log Out", font=("Arial", 12, "bold italic"), fg='white', bg="#B07138", activebackground='red', activeforeground='white', bd=10, width=150, height=40, image=logoutimg,compound='left',command=quitlogin)
    btn8.place(relx=0.5,rely=0.8, relwidth=0.275,relheight=0.12)
    
    rootmain.mainloop()
#mainpage()
