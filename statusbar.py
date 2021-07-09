from tkinter import *



def upload():
    Statusvar.set("busy...")
    #Sbar.update()
    import time
    time.sleep(2)
    Statusvar.set("redy now")


root=Tk()
root.geometry("633x344")

Statusvar=StringVar()

Statusvar.set("REady")
Sbar=Label(root,textvariable=Statusvar,anchor="w").pack(side=BOTTOM,fill=X)

Button(text="upload",command=upload).pack()






root.mainloop()
