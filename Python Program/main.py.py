from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import pyautogui
import tkinter as tk
import tkinter.font as font
import pyttsx3
import random
main = Tk()
text = Text(main,height=4,width=41)
texts = Text(main,height=5,width=44)
count = 0
menubar = Menu(main)
ent=Entry(main)
namevar=StringVar()
main.title("ADVISOR")
main.geometry("700x450")
def hello():
    messagebox.showinfo("About","Here you can generate a password with different lengths. Screenshot button help you to take screenshot of the window. By pressing hello button you can observe text to speech recognition concept.After giving username it allows you to select the length of the password you required.After pressing enter button password will be displayed.If you are not satisfied or you want password with different length press reset button.")
def close():
    main.destroy()
def warning():
    messagebox.showwarning("WARNING","Don't share your passwords")
def click():
    converter=pyttsx3.init()
    converter.setProperty("rate",195)
    converter.setProperty("volume",0.8)
    converter.say("hello,Welcome to password advisor")
    converter.runAndWait()
def submit():
    name=uname_input.get()
    if (len(name) == 0):
        messagebox.showerror("Error","Please enter your name")
    else:
        names=name
        message=name+"!!Follow instructions to get your required password.After submitting your Username you will get generate button.Press that to get your password"
        text.insert(INSERT,message)
        text.place(x=58,y=160)
        messagebox.showinfo("Next",message)
        generate=Button(main,text="Generate",fg="blue",command=password)
        generate.place(x=150,y=240)
def password() :
    length=Label(main,text="Enter the length of the password",fg="black",font=fontname)
    length.place(x=50,y=270)
    number=tk.IntVar()
    global length_input
    length_input=ttk.Combobox(main,width=5,textvariable=number,state="readonly",values=('8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25'))
    length_input.place(x=275,y=270)
    enter = Button(main,text="Enter",command=enters)
    enter.place(x=337,y=266)
def enters():
    global count
    count = count+1
    counts = str(count)
    m=length_input.get()
    if(len(length_input.get()) == 0):
        messagebox.showerror("Error","enter the length")
    elif(count!=1):
       messagebox.showwarning("Warning","You have already choosen the length")
    else:
        n=int(m)
        sai ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=:,?/?><{}[]|"
        sou=" "
        chars=" "
        k= n
        for w in range(k):
            chars = random.choice(sai)
            sou=sou+chars
        another="\nIf you want another password press reset button.And then give the length and press enter button."
        inserting="Your password is \n"+ sou
        inserting = inserting+another
        texts.insert(INSERT,inserting)
        texts.place(x=58,y=300)
def screenshot():
    myscreenshot=pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myscreenshot.save(file_path)
def reset():
    texts.delete('1.0',END)
    global count
    count = 0
file = Menu(menubar,tearoff=0)
menubar.add_cascade(label="FILE",menu=file)
file.add_command(label="WARNING", command=warning)
file.add_command(label="CLOSE" , command= close)
file.add_separator()
file.add_command(label="EXIT", command=None)
help_ = Menu(menubar,tearoff=0)
menubar.add_cascade(label="HELP", menu = help_)
help_.add_command(label="About", command=hello)
help_.add_separator()
help_.add_command(label="Exit" , command = None)
main.config(menu = menubar)
fontstyle = font.Font(family="Helvetica",size=25,weight="bold",slant="italic")
photo = PhotoImage(file = r"C:\Users\APPLE MAC 5656\Desktop\python\volume.png")
pic = photo.subsample(60,60)
heading = Label(main, text="PASSWORD ADVISOR" ,fg="red",font = fontstyle)
heading.pack()
speak= Button(main,text="Hello",command=click,fg="blue",image=pic,compound=LEFT)
speak.pack(side=TOP)
fontname=font.Font(family="Helvetica",size=10,weight="bold")
Uname=Label(main,text="UserName",fg="black",font=fontname).place(x=50,y=120)
uname_input=Entry(main,width=30,textvariable=namevar,font=('calibre',10,'normal'))
uname_input.place(x=126,y=120)
Uname_submit=Button(main,text="Submit",fg="black",command=submit)
Uname_submit.place(x=350,y=117)
screenshotimage=PhotoImage(file=r"C:\Users\APPLE MAC 5656\Desktop\python\camera.png")
camera=screenshotimage.subsample(10,10)
photo=Button(main,text="Take a Screenshot",bg="light green",fg="maroon",command=screenshot,compound=LEFT,image=camera)
photo.place(x=425,y=112)
reset=Button(main,text="Reset",command=reset,fg="white",bg="green")
reset.place(x=585,y=115)


main.mainloop()
