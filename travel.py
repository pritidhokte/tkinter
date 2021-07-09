from tkinter import *
root=Tk()
root.geometry("633x344")
def getvals():
    print("works")
    a=print(f"{nmvalue.get(),phonevalue.get(),genderval.get(),emerval.get(),payval.get()}")

    with open("a.txt","a")as f:
          f.write(f"{nmvalue.get(),phonevalue.get(),genderval.get(),emerval.get(),payval.get()}\n")

Label(text="WELCOME TO TRAVES",bg="black",fg="white").grid(column=3) 
name=Label(root,text="name").grid(row=1,column=2)
phone=Label(root,text="phone").grid(row=2,column=2)
gender=Label(root,text="gender").grid(row=3,column=2)
emer=Label(root,text="emer").grid(row=4,column=2)
pay=Label(root,text="pay").grid(row=5,column=2)

nmvalue=StringVar()
phonevalue=StringVar()
genderval=StringVar()
emerval=StringVar()
payval=StringVar()

useren=Entry(root,textvariable=nmvalue).grid(row=1,column=3)
phoneen=Entry(root,textvariable=phonevalue).grid(row=2,column=3)
genderen=Entry(root,textvariable=genderval).grid(row=3,column=3)
emeren=Entry(root,textvariable=emerval).grid(row=4,column=3)
payen=Entry(root,textvariable=payval).grid(row=5,column=3)
Button(text="submit",command=getvals).grid(row=6,column=3)
root.mainloop()
