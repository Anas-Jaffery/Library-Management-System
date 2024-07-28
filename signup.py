from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import os
import pymysql


def StudentRegister():

    Password =  Password_entry.get()
    Name = Name_entry.get()
    Email = Email_entry.get()
    Phone = Phone_entry.get()
    Address = Address_entry.get()
    

    REGISTER = "insert into "+StudentTable+" values('"+Password+"','"+Name+"','"+Phone+"','"+Email+"','"+Address+"')"
    try:
        cur.execute(REGISTER)
        con.commit()
        messagebox.showinfo("You are registered successfully!")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    root.destroy()
    os.system("python main.py")

def signup():
    global Password_entry,Name_entry,Email_entry,Phone_entry,Address_entry,root,StudentTable,con,cur

    root = Tk()
    root.geometry('600x500')
    root.title("Registration Form")

    mypass = "root"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
    cur = con.cursor()

    same=True
    n=0.25

# Adding a background image
    background_image =Image.open("lib.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
    
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \nSign Up Form", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    StudentTable = "student"


    Password = Label(root, text="Password (Integer)",width=15,font=("bold", 10))
    Password.place(x=150,y=150)
    Password_entry = Entry(root,show="*")
    Password_entry.place(x=290,y=150)

    Name = Label(root, text="Name",width=15,font=("bold", 10))
    Name.place(x=150,y=200)
    Name_entry = Entry(root)
    Name_entry.place(x=290,y=200)

    Email = Label(root, text="Email",width=15,font=("bold", 10))
    Email.place(x=150,y=250)
    Email_entry = Entry(root)
    Email_entry.place(x=290,y=250)

    Phone = Label(root, text="Phone",width=15,font=("bold", 10))
    Phone.place(x=150,y=300)
    Phone_entry = Entry(root)
    Phone_entry.place(x=290,y=300)

    Address = Label(root, text="Address",width=15,font=("bold", 10))
    Address.place(x=150,y=350)
    Address_entry = Entry(root)
    Address_entry.place(x=290,y=350)

    Button(root, text='Submit',width=20,bg='brown',fg='white',command=StudentRegister).place(x=180,y=380)
    
    # it is use for display the registration form on the window
    root.mainloop()


signup()