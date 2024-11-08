from tkinter import *
import mysql.connector as mydb
import hashlib
from tkinter import messagebox
from mainpage import *

def quitlogin():
        mywin.destroy()

        
def login():
        
        mycon = mydb.connect(host="localhost",user="root",password=mypass,database=mydatabase)
        mycur = mycon.cursor()
        u=user.get()
        p=pwd.get()

        query="select * from login where username='"+u+"' and  password=('"+p+"')"
	
        mycur.execute(query)
        mydata = mycur.fetchone()
	
        if mycur.rowcount==1:
                messagebox.showinfo('Login','Login Successful')
                mywin.destroy()
                mainpage()
        else:
                messagebox.showinfo('Login','Access Denied!! Check your username and password')


def loginpage():
        
        global mywin,user,pwd,mypass,mydatabase
        
        # Add your own database name and password here to reflect in the code
        mypass = "root"
        mydatabase="db"

        
        mywin = Tk()
        mywin.title("User Authentication")
        mywin.minsize(width=400,height=400)
        mywin.geometry("600x500")
        # Take n greater than 0.25 and less than 5
        same=True
        n=4.9

        # Adding a background image
        background_image =Image.open("loginbg.jpg")
        [imageSizeWidth, imageSizeHeight] = background_image.size

        newImageSizeWidth = int(imageSizeWidth*n)
        if same:
            newImageSizeHeight = int(imageSizeHeight*n) 
        else:
            newImageSizeHeight = int(imageSizeHeight/n) 
    
        background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.LANCZOS)
        img = ImageTk.PhotoImage(background_image)

        Canvas1 = Canvas(mywin)

        Canvas1.create_image(300,340,image = img)      
        Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
        Canvas1.pack(expand=True,fill=BOTH)

        user=StringVar()
        pwd=StringVar()
        
        headingFrame1 = Frame(mywin,bg="purple",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

        headingLabel = Label(headingFrame1, text="Login Information", bg='light pink', fg='black', font=('Courier',22,'bold'))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(mywin,bg='lemon chiffon',bd=5)
        labelFrame.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.25)   
        
        lb1 = Label(labelFrame,text="User Name : ", bg='lemon chiffon', fg='black',font=('Courier',14,'bold'))
        lb1.place(relx=0.05,rely=0.2)
        
        user1 = Entry(labelFrame,textvariable=user)
        user1.place(relx=0.5,rely=0.2, relwidth=0.4, relheight=0.2)
        user1.focus_set()

        lb2 = Label(labelFrame,text="Password  : ", bg='lemon chiffon', fg='black',font=('Courier',14,'bold'))
        lb2.place(relx=0.05,rely=0.6)
        
        pass1 = Entry(labelFrame,show="*",textvariable=pwd)
        pass1.place(relx=0.5,rely=0.6, relwidth=0.4, relheight=0.2)


        img1=PhotoImage(file='login.png')
        img2=PhotoImage(file='exit.png')

        btn1=Button(mywin,image=img1,height=60, width=120, bg="DodgerBlue3", command=login)
        btn1.place(relx=0.18,rely=0.7, relwidth=0.30,relheight=0.1)

        btn2=Button(mywin,image=img2,height=60, width=120, bg="SpringGreen4",command=quitlogin)
        btn2.place(relx=0.58,rely=0.7, relwidth=0.30,relheight=0.1)
			
        mywin.mainloop()
