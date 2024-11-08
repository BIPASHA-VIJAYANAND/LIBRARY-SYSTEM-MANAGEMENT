from tkinter import *
from PIL import ImageTk,Image
from loginFrame import *

def quitpage():
    mywin.destroy()

def userlogin():
    mywin.destroy()
    loginpage()
    
mywin = Tk()
mywin.title("User Authentication")
mywin.minsize(width=400,height=400)
mywin.geometry("600x500")
# Take n greater than 0.25 and less than 5
same=True
n=1.29

# Adding a background image
background_image =Image.open("image.jpg")
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

headingFrame1 = Frame(mywin,bg="black",bd=5)
headingFrame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.16)

headingLabel = Label(headingFrame1, text="WELCOME TO DAV LIBRARY", bg='pale green', fg='deep pink', font=('Courier',26,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

labelFrame = Frame(mywin,bg='lemon chiffon')
labelFrame.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.5)

lb1 = Label(labelFrame, text=" DONE BY: ",bg='lemon chiffon',fg='black', font=('Courier',20,'bold'))
lb1.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.2)

lb2 = Label(labelFrame, text="V.BIPASHA",bg='lemon chiffon',fg='red2', font=('Courier',15,'bold'))
lb2.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.2)

lb3 = Label(labelFrame, text="S.LAKSHYA",bg='lemon chiffon',fg='red2', font=('Courier',15,'bold'))
lb3.place(relx=0.05,rely=0.5,relwidth=0.9,relheight=0.2)

lb4 = Label(labelFrame, text="KR.SRINIDHI RAJAMANE",bg='lemon chiffon',fg='red2', font=('Courier',15,'bold'))
lb4.place(relx=0.05,rely=0.7,relwidth=0.9,relheight=0.2)

img1=PhotoImage(file='nextpg.png')
img2=PhotoImage(file='exit.png')

btn1=Button(mywin,image=img1,height=60, width=120, bg="black", command=userlogin)
btn1.place(relx=0.125,rely=0.82, relwidth=0.375,relheight=0.1)

btn2=Button(mywin,image=img2,height=60, width=120, bg="SpringGreen4",command=quitpage)
btn2.place(relx=0.525,rely=0.82, relwidth=0.375,relheight=0.1)

mywin.mainloop()




