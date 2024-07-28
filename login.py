from tkinter import *
import pymysql
from tkinter import messagebox
from PIL import ImageTk,Image
import os


def validateLogin():
    
    mypass = "root"
    mydatabase = "db"
    StudentTable = "student"

    con = pymysql.connect(host="localhost", user="root",
                          password="", database=mydatabase)
    cur = con.cursor()

    getstudents = "select * from " + StudentTable
    try:
        cur.execute(getstudents)
        con.commit()
        accountFound = False

        for student in cur:

            if name.get() == str(student[1]) and int(password.get()) == student[0]:
                accountFound = True

        if accountFound:
            os.system("python main.py")

        else:
            messagebox.showinfo("Account not found.")

        tkWindow.destroy()

    except:
        messagebox.showinfo("Failed to fetch files from database")

    return


def login():
    global name, password, tkWindow , root

   

    tkWindow = Tk()
    tkWindow.geometry('500x500')
    tkWindow.title('Library Login Form')

    same=True
    n=0.25

    background_image =Image.open("lib.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
    
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(tkWindow)

    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(tkWindow,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \nLogin Form", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    passwordLabel = Label(tkWindow, text="Password").place(x=120, y=250)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password,
                          show='*').place(x=250, y=250)

    nameLabel = Label(tkWindow, text="Name").place(x=120, y=200)
    name = StringVar()
    nameEntry = Entry(tkWindow, textvariable=name).place(x=250, y=200)

    loginButton = Button(tkWindow, text="Login",
                         command=validateLogin).place(x=260, y=300)
    tkWindow.mainloop()


login()
