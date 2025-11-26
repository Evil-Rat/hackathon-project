import schedule
import time 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import threading
from plyer import notification
from PIL import Image , ImageTk
import pystray


def hide(event): #hides the gui on clicking minimize
    root.withdraw()


def after_click(icon, item): # functions for the tray menu
    if str(item) == "Hide menu":
        root.withdraw()
    elif str(item) == "Show menu":
        root.deiconify()
    elif str(item) == "Exit app":
        root.destroy()
        icon.stop()


def block(event): #stops unwanted events wich cause unexpected behaviour
    return "break"



def validator(input):
    if not input.isdigit() or int(input) > 999 or int(input) < 1 :
        messagebox.showerror("Wrong input", "Please enter a number from 1 to 999")
        return -1
    else:
        return int(input)
    
#uses validator function to set interval
def set_interval():
    global call_job
    global current_interval
    new_interval = validator(interval_pick.get())

    if new_interval == -1: # let the interval be as it was 
        pass
    else:

        interval.set(new_interval)
        schedule.cancel_job(call_job)
        call_job = schedule.every(new_interval).seconds.do(call) # remember to change this to minutes
        interval_pick.delete(0,tk.END)

        current_interval.config(text=f"current interval: {interval.get()} minutes")



def call():
    titles = ["Water reminder", "Drink some water", "Water check", "Water police", "Water alert", "Water break"]


    motivations = ["nice work take a breather and drink some water 😀", "good going, stay hydrated!", "it sure is hot in here, some water would be nice...", "did you know water can make you not thirsty? 🤯",
                   "the human body consists of about 65% water, go drink some! 👽", "GO. DRINK. SOME. WATER. 🔥", "Your body called... it needs water", "Hey, time for a water break!", 
                   "Hey champ, fix that posture and drink some water!", "psst.. hey... CHUG DAT WATER 🔥","drink water in french is bois de l'eau", "Hey, I love you 😘, now go drink some water",
                   "Time to hydrate like there's no tomorrow 😤", "Hey, drink a cup of water you deserve it 🤩" , "What're you still doing here, water is waiting 😆"]
    
    notification.notify(title=random.choice(titles), message=random.choice(motivations), app_name="Flow", app_icon="water-drop.ico", timeout=5)


root = tk.Tk()
title = ttk.Frame(root)
title.pack(side="top")
root.title("Flow")
root.geometry("500x200")
root.resizable(height = False, width = False)
root.bind("<Unmap>", hide) #hides window completely on minimize

main_photo = Image.open("app-icon.png")
main_photo_tk = ImageTk.PhotoImage(main_photo)
main_icon = root.iconphoto(True, main_photo_tk)


ttk.Style().configure("my.TButton", font=("Arial",12,"bold"))

label = tk.Label(title, text = "Flow - Water Reminder", font=("arial",20,"bold"), pady="10")
label.pack()

interval_section = tk.Frame(root)
interval_section.pack()

interval = tk.IntVar(root, value=20)

interval_text= tk.Label(interval_section, text="reminder interval (min) :", font=("Arial",15,"bold"))
interval_text.pack(side="left")

interval_pick = tk.Entry(interval_section, width = 4,font=("Arial",16,"bold"))
interval_pick.pack(side="left", ipadx="10")
interval_pick.bind("<Return>",block ) # this stops the input passing using the enter button

interval_button = ttk.Button(interval_section, style="my.TButton", text="confirm", command=set_interval)
interval_button.pack(side ="right")

current_interval = tk.Label(text=f"current interval: {interval.get()} minutes", pady="10", font=("arial",11,"bold"))
current_interval.pack()




image = Image.open("water-drop.png")

icon = pystray.Icon("main-icon", image, menu = pystray.Menu(
    pystray.MenuItem("Exit app", after_click),
    pystray.MenuItem("Show menu", after_click),
    pystray.MenuItem("Hide menu", after_click)
))

threading.Thread(target=icon.run, daemon=True).start()

call_job = schedule.every(interval.get()).seconds.do(call) #make the user change the time in minutes
def check():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=check, daemon=True).start()

root.mainloop()

#add dark mode
#add a function for the current_interval to show hours and minutes

#add tray hide and show ui functionality
