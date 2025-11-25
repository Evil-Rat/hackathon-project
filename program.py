import schedule
import time 
import tkinter as tk
from tkinter import ttk
import random
import threading



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
    new_interval = validator(interval_pick.get())
    interval.set(new_interval)
    schedule.cancel_job(call_job)
    call_job = schedule.every(new_interval).seconds.do(call)



def call():
    motivations = ["nice work take a breather and drink some water", "good going, stay hydrated!", "it sure is hot in here, some water would be nice...", "did you know water can make you not thirsty?",
                   "the human body consists of about 65% water, go drink some!", "GO DRINK SOME WATER", "Your body called... it needs water", "Hey, time for a water break!", 
                   "Hey champ, fix that posture and drink some water!", "psst.. hey... CHUG DAT WATER"]
    print(random.choice(motivations))


root = tk.Tk()
menu = ttk.Frame(root)
menu.pack(side="top", fill="x")
root.title("healthy work")
root.geometry("500x200")
root.resizable(height = False, width = False)
ttk.Style().configure("my.TButton", font=("Arial",16,"bold"))

# button1 = ttk.Button(menu, text ="click now", style="my.TButton")
# button1.pack(fill="x" ,side="left")
# button2 = ttk.Button(menu, text = "place holder" , style="my.TButton") 
# button2.pack(fill="x",)   

interval_section = tk.Frame(root)
interval_section.pack()
interval = tk.IntVar(root, value=1)


interval_pick = tk.Entry(interval_section, width = 4,font=("Arial",16,"bold"))
interval_pick.pack()

interval_button = ttk.Button(interval_section, style="my.TButton", text="confirm", command=set_interval)
interval_button.pack()


call_job = schedule.every(interval.get()).seconds.do(call) #make the user change the time in minutes
def check():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=check, daemon=True).start()

root.mainloop()

