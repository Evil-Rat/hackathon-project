import schedule
import time 
import tkinter as tk
from tkinter import ttk
import random
import threading


def block(event): #stops unwanted events
    return "break"



def validator(input):
    if not input.isdigit() or int(input) > 999 or int(input) < 1 or input == None:
        #add a thing that says you entered a wrong number and it's now set to the default
        input = 20
        return input
    else:
        return int(input)
    
#uses validator function to set interval
def set_interval():
    global call_job
    global current_interval
    new_interval = validator(interval_pick.get())
    interval.set(new_interval)
    schedule.cancel_job(call_job)
    call_job = schedule.every(new_interval).seconds.do(call)
    interval_pick.delete(0,tk.END)

    current_interval.destroy()
    current_interval = tk.Label(text=f"current interval: {interval.get()} minutes" , pady = "10")
    current_interval.pack()



def call():
    motivations = ["nice work take a breather and drink some water", "good going, stay hydrated!", "it sure is hot in here, some water would be nice...", "did you know water can make you not thirsty?",
                   "the human body consists of about 65% water, go drink some!", "GO DRINK SOME WATER", "Your body called... it needs water", "Hey, time for a water break!", 
                   "Hey champ, fix that posture and drink some water!", "psst.. hey... CHUG DAT WATER"]
    print(random.choice(motivations)) # change this to give system notification


root = tk.Tk()
title = ttk.Frame(root)
title.pack(side="top")
label = tk.Label(title, text = "Flow - Water Reminder", font=("arial",20,"bold"), pady="10")
label.pack()
root.title("Flow")
root.geometry("500x200")
root.resizable(height = False, width = False)




ttk.Style().configure("my.TButton", font=("Arial",12,"bold"))
# button1 = ttk.Button(menu, text ="click now", style="my.TButton")
# button1.pack(fill="x" ,side="left")
# button2 = ttk.Button(menu, text = "place holder" , style="my.TButton") 
# button2.pack(fill="x",)   

interval_section = tk.Frame(root)
interval_section.pack()
interval = tk.IntVar(root, value=1)

interval_text= tk.Label(interval_section, text="reminder interval (min) :", font=("Arial",15,"bold"))
interval_text.pack(side="left")

interval_pick = tk.Entry(interval_section, width = 4,font=("Arial",16,"bold"))
interval_pick.pack(side="left", ipadx="10")
interval_pick.bind("<Return>",block ) # this stops the input passing using the enter button

interval_button = ttk.Button(interval_section, style="my.TButton", text="confirm", command=set_interval)
interval_button.pack(side ="right")

current_interval = tk.Label(text=f"current interval: {interval.get()} minutes", pady="10")
current_interval.pack()


call_job = schedule.every(interval.get()).seconds.do(call) #make the user change the time in minutes
def check():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=check, daemon=True).start()

root.mainloop()

#add dark mode