from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("633x344")
def my_func():
    print("hey three")
def help():
    print("i will help u")
    tmsg.showinfo(title="here",message="i will help u")

def rate_us():
    print("rate us")
    valu=tmsg.askquestion("was ur experience good","was ur experience good")#for shoow msg box in yes ad no
    print(valu)
    if valu=="yes":
        msg="great.rate us on store"
    else:
        msg="tell us was went wrong .we will call you soon"
    tmsg.showinfo("experience",msg)


def divya():
    ans=tmsg.askretrycancel("divya se dosti kr lo","dosti krloo")
    if ans:
        print("retey pe kuch nhi hoga")
    else:
         print("cancle kr diy")
#for drop downmenu
Mainmenu=Menu(root)
m1=Menu(Mainmenu,tearoff=0)# for not showing---in dropdown 
m1.add_command(label="newproj",command=my_func)
m1.add_command(label="save",command=my_func)
m1.add_separator()
m1.add_command(label="saveas",command=my_func)
Mainmenu.add_cascade(label="file",menu=m1)


m2=Menu(Mainmenu,tearoff=0)# for not showing---in dropdown 
m2.add_command(label="changefont",command=my_func)
m2.add_command(label="resize",command=my_func)
m2.add_command(label="delete",command=my_func)
Mainmenu.add_cascade(label="edit",menu=m2)
root.config(menu=Mainmenu)

m3=Menu(Mainmenu,tearoff=0)# for not showing---in dropdown 

m3.add_command(label="help",command=help)
m3.add_command(label="rateus",command=rate_us)
m3.add_command(label="try",command=divya)
Mainmenu.add_cascade(label="help",menu=m3)

root.config(menu=Mainmenu)






root.mainloop()
