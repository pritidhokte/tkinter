from tkinter import *
root=Tk()
root.geometry("633x344")
def getvals():
    print(uservalue.get())
    print(passvalue.get())
username=Label(root,text="username").grid()
passwor=Label(root,text="password").grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

useren=Entry(root,textvariable=uservalue).grid(row=0,column=1)

passen=Entry(root,textvariable=passvalue).grid(row=1,column=1)
Button(text="submit",command=getvals).grid()
root.mainloop()
