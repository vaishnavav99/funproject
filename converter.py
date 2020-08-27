import os
from moviepy.editor import *
import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox, filedialog 
from ttkthemes import ThemedStyle
from PIL import Image

def Widgets():

        def c2():
            mytext = ent1.get()
            d=Path1.get()
            if(d=='' or mytext ==''):
                messagebox.showinfo("Error",  
                        "\n" 
                        + "Field empty")
            i=Image.open(d)
            x=mytext+'.jpg'
            i.save(x)
            messagebox.showinfo("Done",  
                        "\n" 
                        + "Converted Successfully")
            e1.delete(0,'end')
            t1.delete(0,'end')
        
        def c1():
            mytext = ent.get()
            d=Path.get()
            if(d=='' or mytext ==''):
                messagebox.showinfo("Error",  
                        "\n" 
                        + "Field empty")
            i=Image.open(d)
            x=mytext+'.png'
            i.save(x)
            messagebox.showinfo("Done",  
                        "\n" 
                        + "Converted Successfully")
            e.delete(0,'end')
            t.delete(0,'end')


        def clear():
            entry1.delete(0,'end')
            root.destinationText.delete(0,'end')


        def c():
            mytext = entry.get()
            d=download_Path.get()
            if(d=='' or mytext ==''):
                messagebox.showinfo("Error",  
                        "\n" 
                        + "Field empty")
                
            
            print (d)
            video = VideoFileClip(os.path.join(d))
            x=mytext+'.mp3'
            video.audio.write_audiofile(os.path.join(x))
            video.audio.close()
            video.close
            messagebox.showinfo("Done",  
                        "\n" 
                        + "Converted Successfully")
            clear()

        def Browse2():
            download_Directory1 = filedialog.askopenfilename(initialdir="YOUR FILE PATH")
            Path1.set(download_Directory1)

        def Browse1():
            download_Directory = filedialog.askopenfilename(initialdir="YOUR FILE PATH")
            Path.set(download_Directory)
        def Browse(): 
    # Presenting user with a pop-up for 
    # directory selection. initialdir  
    # argument is optional Retrieving the 
    # user-input destination directory and 
    # storing it in downloadDirectory 
            download_Directory = filedialog.askopenfilename(initialdir="YOUR FILE PATH") 
   
    # Displaying the directory in the directory 
    # textbox 
            download_Path.set(download_Directory) 
            

        frame = Frame(root)
        frame.grid()
        tabControl = ttk.Notebook(root,cursor="hand2")
        tabControl.configure(width=400, height=200)

       
        a_tab = tk.Frame(tabControl,bg="#d2ffd2",cursor="hand2")
        tabControl.add(a_tab, text="MP4 to MP3")
        tabControl.grid()

        b_tab = tk.Frame(tabControl,bg="#000000",cursor="hand2")
        tabControl.add(b_tab, text="Photo")
        tabControl.grid()

        about_tab = tk.Frame(tabControl,bg="#d2ffd2")
        tabControl.add(about_tab, text="About")
        tabControl.grid()

        frame = Frame(b_tab)
        frame.grid()
        tabControl1 = ttk.Notebook(b_tab,)
        tabControl1.configure(width=368, height=150)
################################################################################
        a1_tab = tk.Frame(tabControl1,bg="#d2ffd2",cursor="hand2")
        tabControl1.add(a1_tab, text="JPG to PNG")
        tabControl1.place(x=14,y=10)

        label1 = tk.Label(a1_tab, text="Path", bg="#d2ffd2", fg='#000000')
        label1.place(x=10,y=15)

        t = ttk.Entry(a1_tab, 
                                 width=25, 
                                 textvariable=Path) 
        t.place(x=60,y=15)
        browse_B = Button(a1_tab,  
                      text="Browse", 
                      command=Browse1, 
                      width=10, 
                      ) 
        browse_B.place(x=240,y=10)

        label1 = tk.Label(a1_tab, text="Output File Name :", bg="#d2ffd2", fg='#000000')
        label1.place(x=10,y=70)

        e = ttk.Entry(a1_tab, width=23, textvariable=ent)
        e.place(x=150,y=70)

        label1 = tk.Label(a1_tab, text=" .png", bg="#d2ffd2", fg='#000000')
        label1.place(x=270,y=70)

        button = Button(a1_tab,text="Convert",command=c1)
        button.place(x=160,y=110)
###############################################################################
        b1_tab = tk.Frame(tabControl1,bg="#d2ffd2",cursor="hand2")
        tabControl1.add(b1_tab, text="PNG to JPG")
        tabControl1.place(y=10)

        label1 = tk.Label(b1_tab, text="Path", bg="#d2ffd2", fg='#000000')
        label1.place(x=10,y=15)

        t1 = ttk.Entry(b1_tab, 
                                 width=25, 
                                 textvariable=Path1) 
        t1.place(x=60,y=15)
        browse_B1 = Button(b1_tab,  
                      text="Browse", 
                      command=Browse2, 
                      width=10, 
                      ) 
        browse_B1.place(x=240,y=10)

        label1 = tk.Label(b1_tab, text="Output File Name :", bg="#d2ffd2", fg='#000000')
        label1.place(x=10,y=70)

        e1 = ttk.Entry(b1_tab, width=23, textvariable=ent1)
        e1.place(x=150,y=70)

        label1 = tk.Label(b1_tab, text=" .jpg", bg="#d2ffd2", fg='#000000')
        label1.place(x=270,y=70)

        button = Button(b1_tab,text="Convert",command=c2)
        button.place(x=160,y=110)
        
###############################################################################

        label1 = tk.Label(about_tab, text="Created by Vaishnav A V", bg="#d2ffd2", fg='#000000')
        label1.place(x=20,y=20)

        label2 = tk.Label(about_tab, text="easy convert", bg="#d2ffd2", fg='#000000')
        label2.place(x=20,y=60)

        label3 = tk.Label(about_tab, text="https://vaishnavav99.github.io/Vaishnav/", bg="#d2ffd2", fg='#000000')
        label3.place(x=20,y=100)


        label1 = tk.Label(a_tab, text="Enter File Name :", bg="#d2ffd2", fg='#000000')
        label1.place(x=30,y=100)

        entry1 = ttk.Entry(a_tab, width=20, textvariable=entry)
        entry1.place(x=150,y=100)

        label1 = tk.Label(a_tab, text=" .mp3", bg="#d2ffd2", fg='#000000')
        label1.place(x=280,y=100)

        label1 = tk.Label(a_tab, text="Input File Path", bg="#d2ffd2", fg='#000000')
        label1.place(x=20,y=10)

        root.destinationText = ttk.Entry(a_tab, 
                                 width=40, 
                                 textvariable=download_Path) 
        root.destinationText.place(x=120,y=10)
        browse_B = Button(a_tab,  
                      text="Browse", 
                      command=Browse, 
                      width=10, 
                      ) 
        browse_B.place(x=270,y=40)

        button = Button(a_tab,text="Convert",command=c)
        button.place(x=160,y=150)



root = tk.Tk() 
   
# Setting the title, background color  
# and size of the tkinter window and  
# disabling the resizing property 
root.resizable(False, False)
root.title("Convert")
style = ThemedStyle(root)
style.theme_use("radiance") 
root.geometry("+25+25") 
root.iconphoto(False, tk.PhotoImage(file='c.png'))  
# Creating the tkinter Variables  
download_Path = StringVar()
Path = StringVar() 
Path1 = StringVar()
entry = StringVar()
ent = StringVar()
ent1 = StringVar()
# Calling the Widgets() function 
Widgets() 
   
# Defining infinite loop to run 
# application 
root.mainloop()