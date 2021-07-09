from tkinter import *
root=Tk()
root.geometry("633x344")
def my_func():
    print("hey three")
#use to these to create non dropdown menu
'''mymenu=Menu(root)
mymenu.add_command(label="File",command=my_func)
mymenu.add_command(label="exit",command=quit)
'''
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







root.mainloop()
