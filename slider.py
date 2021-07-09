from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("633x344")
def goo():
    with open("z.txt",'a')as f:
        f.write(  str(myslider2.get()))
        with open("z.txt")as f:
            f.read()
            print()
            tmsg.showinfo("your dollors is","thanks for rating us")
def getd():
    print(f"we have created {myslider2.get()} dollor to ur bank")
    tmsg.showinfo("dollors",f"we have created {myslider2.get()} dollor to ur bank")
'''myslider=Scale(root,from_=0, to=455)
myslider.pack()'''
Label(text="how many dollers u want").pack()
myslider2=Scale(root,from_=0, to=100,orient=HORIZONTAL,tickinterval=50)
#myslider2.set(30)
myslider2.pack()
Button(text="get dollars",command=goo,pady=10).pack()

  









root.mainloop()
