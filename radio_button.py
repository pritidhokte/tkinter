from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("633x344")

def order():
    s=var.get()
    tmsg.showinfo("order received",f"we have received ur order for {s} ,Thamks for ordering")
  


var=StringVar()
var.set("radio")



Label(root,text="what would u like to have",font="lucida",justify="left").pack()                 
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value="Samosa").pack(anchor="w")
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack(anchor="w")


Button(text="order now",command=order).pack()

root.mainloop()
