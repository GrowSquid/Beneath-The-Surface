import tkinter as Tkinter 
from datetime import datetime
counter = 72000
running = False
def counter_label(label): 
    def count(): 
        if running: 
            global counter

# Found a delay when launching, this creates a net to prevent late timing
            if counter==72000:
                output="Starting..."
            else:
                time=datetime.fromtimestamp(counter)
                string = time.strftime("%H:%M:%S")
                output=string

            label.config(text=output)
#Stopwatch is in seconds, so the counter goes up every 1000 ms
            label.after(1000, count)  
            counter += 1

    count()

def Begin(label):
    global running
    running = True
    counter_label(label)
    Begin['state']='normal'
    Stop['state']='disabled'
    Reset['state']='normal'

def Stop():
    global running
    Begin['state']='normal'
    Stop['state']='disabled'
    Reset['state']='normal'
    running = False

def Reset(label):
    global counter
    counter=72000
    
# if reset is selected when not running
    if running == False:
        Reset['state']='disabled'
        label['text']='Welcome!'

#if reset is selected when running
    else:
        label['text']='Starting..'

root = Tkinter.Tk()
root.title

#making the GUI compact and lightweight
root.minsize(width=250, height=70) 
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold") 
label.pack() 
f = Tkinter.Frame(root)
begin = Tkinter.Button(f, text='Begin', width=6, command=lambda:Begin(label)) 
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop) 
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label)) 
f.pack(anchor = 'center',pady=5)
begin.pack(side="left") 
stop.pack(side ="left") 
reset.pack(side="left") 
root.mainloop()
