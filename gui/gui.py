##
from tkinter import *
from tkinter import messagebox
def fnok():
     fname =e1.get()
     lname=e2.get()
     
     messagebox.showinfo("output","fullname is %s "%(fname+lname))  #it shows msg format
def fncancel():
     win.destroy()##close the applictions
     
win=tk()
win.title("tex widget")
win.geometry("250x250")
l1=Label(win,text="frist name:")
l1.grid(row=0,column=0)
e1= Entry(win)
e1.grid(row=0,column=1)

l2=Label(win,text="last name:")
l2.grid(row=1,column=0)
e2= Entry(win)
e2.grid(row=1,column=1)

b1= Button(win,text="ok",command=fnok)
b1.grid(row=2,column=0)

b2= Button(win,text="cancel",command=fncancel)
b2.grid(row=2,column=1)

win.mainloop()
