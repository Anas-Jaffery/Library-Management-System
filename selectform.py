from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os

def opensignup():
    os.system("python signup.py")
    root1.destroy()

def openlogin():
    os.system("python login.py")
    root1.destroy()




def selectform():
    global root1

    root1= Tk()
    root1.geometry('600x500')
    root1.title("Selection Form")

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

    Canvas1 = Canvas(root1)

    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root1,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Select your Option", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    Button(root1, text='Signup ',width=20,bg='brown',fg='white',command=opensignup).place(x=100,y=380)
    Button(root1, text='Login ',width=20,bg='brown',fg='white',command=openlogin).place(x=300,y=380)

    root1.mainloop()

selectform()