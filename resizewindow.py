from tkinter import *
def update():
    print("updating....")
    root.geometry(f"{width.get()}x{height.get()}")
root=Tk()
root.geometry("455x233")
width=StringVar()
height=StringVar()
Label(text="widht").pack(anchor="w")
Entry(root,textvariable=width).pack()
Label(text="height").pack(anchor="w")

Entry(root,textvariable=height).pack()
Button(text="resize",command=update).pack()
root.mainloop()
