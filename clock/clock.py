
# importing whole module
import os 
from tkinter import * 
import tkinter as tk
from tkinter.ttk import *
from datetime import date
# importing strftime function to 
# retrieve system's time 
from time import strftime 
from tkinter import ttk
import time as tm
from tkinter import messagebox
  
# creating tkinter window 
root = Tk() 
root.title('Clock') 
root.resizable(False, False)
frame = Frame(root)
frame.grid()
tabControl = ttk.Notebook(root,cursor="hand2")
tabControl.configure(width=400, height=200)

datet = tk.Frame(tabControl,bg="#d2ffd2",cursor="hand2")
tabControl.add(datet, text="Date")
tabControl.grid()

clock = tk.Frame(tabControl,bg="#d2ffd2",cursor="hand2")
tabControl.add(clock, text="Time")
tabControl.grid()

alarm = tk.Frame(tabControl,bg="#d2ffd2",cursor="hand2")
tabControl.add(alarm, text="Alarm")
tabControl.grid()

countd = tk.Frame(tabControl,bg="#d2ffd2",cursor="hand2")
tabControl.add(countd, text="Countdown")
tabControl.grid()

stopw = tk.Frame(tabControl,bg="#d2ffd2",cursor="hand2")
tabControl.add(stopw, text="Stopwatch")
tabControl.grid()

about = tk.Frame(tabControl,bg="#d2ffd2",cursor="hand2")
tabControl.add(about, text="About")
tabControl.grid()

lbb = Label(about,text="Vaishnav A V", font = ('calibri', 20, 'bold'), 
            background = '#d2ffd2', 
            foreground = 'dark green')
lb = Label(about,text="vaishnavav99.github.io/Vaishnav/", font = ('calibri', 15, 'bold'), 
            background = '#d2ffd2', 
            foreground = 'green4')  
# Placing date at the centre 
lbb.place(relx=0.3,rely=0.3)
lb.place(relx=0.15,rely=0.45)

t = date.today()
lbl2 = Label(datet,text=t.strftime("%d/%m/%Y"), font = ('calibri', 40, 'bold'), 
            background = '#d2ffd2', 
            foreground = 'dark green') 
lbl3 = Label(datet,text=t.strftime("%A"), font = ('calibri', 25, 'bold'), 
            background = '#d2ffd2', 
            foreground = 'green4')  
# Placing date at the centre 
# of the tkinter window 
lbl2.place(x=60,y=50)
lbl3.place(x=220,y=110)

  
# This function is used to  
# display time on the label 
def time():
    if (form==1): 
        string = strftime('%I:%M:%S %p')
        lbl.config(text = string)
    else:
        string = strftime('%H:%M:%S')
        lbl.config(text = "    "+ string) 
    lbl.after(1000, time) 

def format():
    global form
    if form==1:
        form=0
        btnc['text']='12hour'
    else:
        form=1
        btnc['text']='24hour'
    
    

# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(clock, font = ('calibri', 40, 'bold'), 
            background = '#d2ffd2', 
            foreground = 'green') 
form=1
# Placing clock at the centre 
# of the tkinter window 
lbl.place(x=60,y=50)
btnc = tk.Button(clock,width =10, text='24hour',
			command= format,fg="blue")
btnc.place(x = 160,y = 140)
time() 
  

from datetime import datetime 
counter = 66600
running = False
def counter_label(label):  
    def count():  
        if running:  
            global counter  
    
            # To manage the intial delay.  
            if counter==66600:              
                display="Starting..."
            else: 
                tt = datetime.fromtimestamp(counter) 
                string = tt.strftime("%H:%M:%S") 
                display=string  
    
            label['text']=display   # Or label.config(text=display)  
    
            # label.after(arg1, arg2) delays by   
            # first argument given in milliseconds  
            # and then calls the function given as second argument.  
            # Generally like here we need to call the   
            # function in which it is present repeatedly.  
            # Delays by 1000ms=1 seconds and call count again.  
            label.after(1000, count)   
            counter += 1
    
    # Triggering the start of the counter.  
    count()       
    
# start function of the stopwatch  
def Start(label):  
    global running  
    running=True
    counter_label(label)  
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    
# Stop function of the stopwatch  
def Stop():  
    global running  
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
    
# Reset function of the stopwatch  
def Reset(label):  
    global counter  
    counter=66600
    
    # If rest is pressed after pressing stop.  
    if running==False:
        tt = datetime.fromtimestamp(counter) 
        string = tt.strftime("%H:%M:%S")        
        reset['state']='disabled'
        label['text']=string
    
    # If reset is pressed while the stopwatch is running.  
    else:                 
        label['text']='Starting...'
tt = datetime.fromtimestamp(counter) 
string = tt.strftime("%H:%M:%S") 
label = tk.Label(stopw, text=string, foreg="green",background = '#d2ffd2', font="Verdana 30 bold")  
label.place(x=100,y=40)  
 
start = tk.Button(stopw, text='Start', width=6, command=lambda:Start(label),fg="blue")  
stop = tk.Button(stopw, text='Stop',width=6,state='disabled', command=Stop,fg="blue")  
reset = tk.Button(stopw, text='Reset',width=6, state='disabled', command=lambda:Reset(label),fg="blue")  


start.place(x=120,y=100)
stop.place(x=170,y=100)
reset.place(x=220,y=100)

hour=StringVar()
minute=StringVar()
second=StringVar()

# setting the default value as 0
hour.set("0")
minute.set("0")
second.set("0")
temp=0
l = tk.Label(countd, text='Please enter Count(hr,min,sec)', foreg="dark green",background = '#d2ffd2',font=("Arial",14,"bold"),)
l.place(x=50,y=30)

# Use of Entry class to take input from the user
hourl = tk.Label(countd, text='Hr:', foreg="green4",background = '#d2ffd2',font=("Arial",18,"bold"),)
hourl.place(x=50,y=80)
hourEntry= Entry(countd, width=3, font=("Arial",18,""),
				textvariable=hour)
hourEntry.place(x=90,y=80)
minl = tk.Label(countd, text='Min:', foreg="green4",background = '#d2ffd2',font=("Arial",18,"bold"),)
minl.place(x=140,y=80)
minuteEntry= Entry(countd, width=3, font=("Arial",18,""),
				textvariable=minute)
minuteEntry.place(x=200,y=80)
secl = tk.Label(countd, text='Sec:', foreg="green4",background = '#d2ffd2',font=("Arial",18,"bold"),)
secl.place(x=250,y=80)
secondEntry= Entry(countd, width=3, font=("Arial",18,""),
				textvariable=second)
secondEntry.place(x=310,y=80)

def r():
    l['text']=' Please enter Count(hr,min,sec)'
    messagebox.showinfo("Time Countdown", "Time's up ")
def submit():
	try:
		# the input provided by the user is
		# stored in here :temp
		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		print("Please input the right value")
	while temp >-1:
		l['text']='  Running...'
		# divmod(firstvalue = temp//60, secondvalue = temp%60)
		mins,secs = divmod(temp,60) 

		# Converting the input entered in mins or secs to hours,
		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
		# 50min: 0sec)
		hours=0
		if mins >60:
			
			# divmod(firstvalue = temp//60, secondvalue 
			# = temp%60)
			hours, mins = divmod(mins, 60)
		
		# using format () method to store the value up to 
		# two decimal places
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		# updating the GUI window after decrementing the
		# temp value every time
		countd.update()
		tm.sleep(1)

		# when temp value = 0; then a messagebox pop's up
		# with a message:"Time's up"
		if (temp == 0):
			r()
		# after every one sec the value of temp will be decremented
		# by one
		temp -= 1

# button widget
btn = tk.Button(countd,width =10, text='Start',
			command= submit,fg="blue")
btn.place(x = 160,y = 140)


def SubmitButton():
  AlarmTime= entry1.get()
  Message1()
  #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
  CurrentTime = tm.strftime("%H:%M")
  print("the alarm time is: {}".format(AlarmTime))
  #label2.config(text="")
  while AlarmTime != CurrentTime:
    #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
    CurrentTime = tm.strftime("%H:%M")
    tm.sleep(1)
  if AlarmTime == CurrentTime:
     print("now Alarm Musing Playing")
     from playsound import playsound
     playsound('alarm.mp3')
     label2.config(text = "Alarm music playing.....")
     entry1.insert(3,"example - 16:15 [HH:MM]")
     messagebox.showinfo(title= 'Alarm Message', message= "{}".format(entry2.get()))
def Message1():
    AlarmTimeLable= entry1.get()
    label2.config(text="the Alarm time is Counting...")
    #label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
    messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {}'.format(AlarmTimeLable)) 
label1= tk.Label(alarm,text = "Enter the Alarm time[24 hr format(HH:MM)] :",background = '#d2ffd2')
label1.pack()


entry1 = tk.Entry(alarm, width = 30,)
entry1.pack()

labelAlarmMessage= tk.Label(alarm, text="Alarm Message:",background = '#d2ffd2')
labelAlarmMessage.pack()

entry2= tk.Entry(alarm, width=30)
entry2.pack()

button1= tk.Button(alarm, text= "submit", command=SubmitButton)
button1.pack()
#this Label2 will show the Last Alarm Time
label2= tk.Label(alarm,background = '#d2ffd2')
label2.pack()

    
#label2.config(text="hello")

mainloop()