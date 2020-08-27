import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import pyttsx3
import pyttsx3.drivers
import os
from playsound import playsound


def Widgets():
        
        def clear():
            entry1.delete(1.0,'end')
            


        def speak():
            mytext = entry1.get("1.0","end-1c")
            engine = pyttsx3.init()
 
            engine.say(mytext)
            engine.setProperty('rate', 120)
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
            clear()
            

        frame = Frame(root)
        frame.grid()
        tabControl = ttk.Notebook(root)
        tabControl.configure(width=400, height=200)

        talk_tab = ttk.Frame(tabControl)
        tabControl.add(talk_tab, text="Talk")
        tabControl.grid()
        about_tab = ttk.Frame(tabControl)
        tabControl.add(about_tab, text="About")
        tabControl.grid()

        

        label1 = Label(about_tab, text="Created by Vaishnav A V")
        label1.grid(column=2, row=0)

        label2 = Label(about_tab, text="A simple way to talk")
        label2.grid(column=2, row=1)

        label3 = Label(about_tab, text="https://vaishnavav99.github.io/Vaishnav/")
        label3.grid(column=2, row=2)


        label1 = Label(talk_tab, text="Enter Sentence")
        label1.place(x=160,y=10)

        entry1 = Text(talk_tab, width=48, height=8)
        entry1.place(x=5,y=30)

        button = Button(talk_tab,text="Talk",command=speak)
        button.place(x=170,y=170)


        

        

# Creating object of tk class 
root = tk.Tk() 
   
# Setting the title, background color  
# and size of the tkinter window and  
# disabling the resizing property 
root.resizable(False, False)
root.title("I can Talk") 
   
# Creating the tkinter Variables 
video_Link = StringVar() 
download_Path = StringVar() 
   
# Calling the Widgets() function 
Widgets() 
   
# Defining infinite loop to run 
# application 
root.mainloop()