####student from
##rigister from
from Tkinter import *
import tkMessageBox
import pymysql

def fnshow():
     Name=e1.get()
     tkMessageBox.showinfo("name of a student","student name___%s"%Name)
     if var.get()==1:
          gender="male"
     elif var.get()==2:
          gender="female"
     tkMessageBox.showinfo("gender","gender is___%s"%gender)
     listcourse=[]
     if(var1.get()==1):
          listcourse.append("python")
     if(var2.get()==1):
          listcourse.append("java")
     if(var3.get()==1):
          listcourse.append("datascince")
     if(var4.get()==1):
          listcourse.append("c++")
          
     tkMessageBox.showinfo("selcted course","course--%s" %listcourse)
     
     print("brach selected:-----",l.get(ACTIVE))
     tkMessageBox.showinfo("selcted name","baranch name___%s"%l.get(ACTIVE))
        
def fnin():
    name=e1.get()
    if var.get()==1:
        gender="male"
    elif var.get()==2:
        gender="female"
    
    if(var1.get()==1):
          course = "python"
    if(var2.get()==1):
          course ="java"
    if(var3.get()==1):
          course="datascince"
    if(var4.get()==1):
          course="c++"
    branch = l.get(ACTIVE)
    
    conn = pymysql.connect(host="localhost", user="root", passwd = "",db="pythondb")
    cur = conn.cursor()
    sql="""insert into rtsdata values(%s,%s,%s,%s)"""
    try:
        cur.execute(sql,(name,gender,course,branch))
        conn.commit()
        print("insert succes in db")
    except:
        conn.rollback()
        print("insert failed in db")

    conn.close()
    
    
def fnud(): #change the course based on the name
    n=e1.get()
    if(var1.get()==1):
          c = "python"
    if(var2.get()==1):
          c ="java"
    if(var3.get()==1):
          c="datascince"
    if(var4.get()==1):
          c="c++"
            
    conn= pymysql.connect(host="localhost",user="root",passwd="",db="pythondb")
    cur=conn.cursor()
    sql="""update rtsdata set course=%s where name=%s"""
    try:
        cur.execute(sql,(c,n))
        conn.commit()
        print("update success in db")
    except:
        conn.rollback()
        print("update failed in db")

    conn.close()
def fndl():
    n1=e1.get()
    conn = pymysql.connect(host="localhost",user="root",passwd="",db="pythondb")
    cur=conn.cursor()
    sql="""delete from rtsdata where name=%s """
    try:
        cur.execute(sql,(n1))
        conn.commit()
        print("delete success in db")
    except:
        conn.rollback()
        print("delete failed in db")
    conn.close()
def fnret():
    name=e1.get()
    print(name)
    conn = pymysql.connect(host="localhost",user="root",passwd="",db="pythondb")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM rtsdata where name=%s",(name))
    result=cursor.fetchone()
    tkMessageBox.showinfo("output","name %s --gender  %s--coure %s --branch%s"%(result[0],result[1],result[2],result[3]))
    print("row selection success",result)
def fnclr():
     win.clear()
def fnexit():
     win.destroy()

win=Tk()
win.title("Rigisterfrom")
win.geometry("500x500")
Label(win,text="Name of a student:").grid(row=0,column=0)
e1= Entry(win)
e1.grid(row=0,column=1)
Label(win,text="Gender:").grid(row=1,column=0)
var = IntVar()
Radiobutton(win,text="male",variable= var,value=1).grid(row=1,column=1)
Radiobutton(win,text="female",variable= var,value=2).grid(row=1,column=2)
Label(win,text="choose ur language:").grid(row=2,column=0)
var1= IntVar()
Checkbutton(win,text="python",variable=var1).grid(row=2,column=1)
var2= IntVar()
Checkbutton(win,text="java",variable=var2).grid(row=2,column=2)
var3= IntVar()
Checkbutton(win,text="datascience",variable=var3).grid(row=3,column=1)
var4= IntVar()
Checkbutton(win,text="c++",variable=var4).grid(row=3,column=2)
Label(win,text="choose branch:").grid(row=4,column=0)
l=Listbox(win,bg="yellow",height=6)
l.insert(1,"BTM")
l.insert(2,"kanigiri")
l.insert(3,"bng")
l.insert(4,"hyb")
l.grid()
Button(win,text="insert",command=fnin).grid(row=8,column=0)
Button(win,text="update",command=fnud).grid(row=8,column=1)
Button(win,text="delete",command=fndl).grid(row=8,column=2)
Button(win,text="retrive",command=fnret).grid(row=8,column=3)
Button(win,text="show",command=fnshow).grid(row=8,column=4)


Button(win,text="clear",command=fnclr).grid(row=20,column=0)
Button(win,text="exit",command=fnexit).grid(row=20,column=2)



win.mainloop()
