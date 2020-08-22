# Python program to test 
# internet speed 

import speedtest 
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('380x320')
root.title('Net Speed')
root.config(background="#000000") 
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file='icon/speed.png'))
def clear():
        ds.delete(1.0,'end')
        us.delete(1.0,'end')
        pg.delete(1.0,'end')
        w.delete(1.0,'end')

def show():
        ds.delete(1.0,'end')
        us.delete(1.0,'end')
        pg.delete(1.0,'end')
        w.insert('end',"||||||||||||||")
        st = speedtest.Speedtest()
        d=(st.download())/1000000
        d1=round(d, 2)
        ds.insert('end',d1)
        u=(st.upload())/1000000
        u1=round(u, 2)
        us.insert('end',u1)
        pg1=st.results.ping
        pg.insert('end',pg1)
        



m_label1 = Label(root,text="Download Speed",font=('verdana','10','bold'),bg="#000000",fg="#FFFFFF")
m_label1.place(x=50,y=20)

ds = Text(root,width=5,height=1,relief=RIDGE,font=('verdana','10','bold'))
ds.place(x=200,y=20)

mbps = Label(root,text="Mbps",font=('verdana','10','bold'),bg="#000000",fg="#FFFFFF")
mbps.place(x=250,y=20)

m_label2 = Label(root,text="Upload Speed",font=('verdana','10','bold'),bg="#000000",fg="#FFFFFF")
m_label2.place(x=50,y=120)

us = Text(root,width=5,height=1,relief=RIDGE,font=('verdana','10','bold'))
us.place(x=200,y=120)

mbps = Label(root,text="Mbps",font=('verdana','10','bold'),bg="#000000",fg="#FFFFFF")
mbps.place(x=250,y=120)


m_label3 = Label(root,text="PING",font=('verdana','10','bold'),bg="#000000",fg="#FFFFFF")
m_label3.place(x=50,y=220)

pg = Text(root,width=5,height=1,relief=RIDGE,font=('verdana','10','bold'))
pg.place(x=200,y=220)

ms = Label(root,text="ms",font=('verdana','10','bold'),bg="#000000",fg="#FFFFFF")
ms.place(x=250,y=220)

show = Button(root,text="Show",font=('verdana',10,'bold'),relief=RIDGE,command=show,bg="#000000",fg="#FFFFFF")
show.place(x=160,y=280)
w = Text(root,width=10,height=1,relief=RIDGE,font=('verdana','8'),bg="#000000",fg="#FFFFFF")
w.place(x=240,y=280)

clear = Button(root,text="Clear",font=('verdana',10,'bold'),relief=RIDGE,command=clear,bg="#000000",fg="#FFFFFF")
clear.place(x=60,y=280)
root.mainloop()