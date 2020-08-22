from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import calendar
root = tk.Tk()
root.geometry('420x330')
root.title('Calender')
root.config(background="#000000") 
root.iconphoto(False, tk.PhotoImage(file='icon/cal.png'))

def show():
        cal.delete(1.0,'end')
        
        m = int(month.get())
        y = int(year.get())
       
        if m >12:
            cal.insert('end',"no such month\nselect between\n   1(January)to 12(December)")
        elif m <1:
            cal.insert('end',"no such month\nselect between\n   1(January)to 12(December)")        
        else:
            
            output = calendar.month(y,m)

            cal.insert('end',output)
def exit():
        root.destroy()





m_label = Label(root,text="please enter month and year",font=('verdana','10'),bg="#000000",fg="#FFFFFF")
m_label.place(x=100,y=40)



m_label = Label(root,text="Month",font=('verdana','10','bold'),bg="#000000",fg="#FFFFFF")
m_label.place(x=70,y=80)

month = Entry(root,width="8") 
month.place(x=140,y=80) 
  
y_label = Label(root,text="Year",font=('verdana','10','bold'),bg="#000000",fg="#FFFFFF")
y_label.place(x=210,y=80)

year = Entry(root,width="10") 
year.place(x=260,y=80) 


cal = Text(root,width=33,height=8,relief=RIDGE,)
cal.place(x=70,y=110)

show = Button(root,text="Show",font=('verdana',10,'bold'),relief=RIDGE,command=show)
show.place(x=120,y=250)



exit = Button(root,text="Exit",font=('verdana',10,'bold'),relief=RIDGE,borderwidth=2,command=exit)
exit.place(x=240,y=250)

m_label = Label(root,text="Vaishnav A V",font=('verdana','8'),bg="#000000",fg="#FFFFFF")
m_label.place(x=300,y=300)
root.mainloop()