from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title('Translator India')
root.geometry('522x30')
root.maxsize(522,350)
root.minsize(522,350)
root.config(background="#000000") 
root.iconphoto(False, tk.PhotoImage(file='icon/gt.png'))

def translate():
        language_1 = t1.get("1.0","end-1c")
        cl = choose_langauge.get()

        if language_1 == '':
                messagebox.showerror('Language Translator','empty')
        else:
                translator = Translator()
                output = translator.translate(language_1, dest=cl)
                t2.insert('end',output.text)

def clear():
        t1.delete(1.0,'end')
        t2.delete(1.0,'end')
        






a = tk.StringVar() 
auto_detect = ttk.Combobox(root, width = 20, textvariable = a, state='readonly',font=('verdana',10,'bold'),) 
  


auto_detect['values'] = (
                          'Auto Detect',
                        'English',
                        'Gujarati',
                        'Hindi',
                        'Malayalam',
                        
                        'Marathi',
                        'Punjabi',
                        
                          ) 
  
auto_detect.place(x=30,y=70)
auto_detect.current(0) 





l = tk.StringVar() 
choose_langauge = ttk.Combobox(root, width = 20, textvariable = l, state='readonly',font=('verdana',10,'bold')) 
  


choose_langauge['values'] = (
                       
                        'English',
                        'Gujarati',
                        'Hindi',
                        'Malayalam',
                        
                        'Marathi',
                        'Punjabi',
                        
                          ) 
  
choose_langauge.place(x=290,y=70)
choose_langauge.current(0) 


t1 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE,)
t1.place(x=10,y=100)

t2 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=260,y=100)


button = Button(root,text="Translate",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=translate)
button.place(x=150,y=280)


clear = Button(root,text="Clear",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=clear)
clear.place(x=280,y=280)

root.mainloop()