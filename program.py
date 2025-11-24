import schedule
import time 
import tkinter as tk
from tkinter import ttk
import random
import threading



def call():
    motivations = ["nice work take a breather and drink some water", "good going, stay hydrated!", "it sure is hot in here, some water would be nice..."]
    print(random.choice(motivations))


schedule.every(5).seconds.do(call)
def check():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=check, daemon=True).start()

root = tk.Tk()
menu = ttk.Frame(root)
menu.pack(side="top", fill="x")
root.title("healthy work")
root.geometry("500x200")
root.resizable(height = False, width = False)
ttk.Style().configure("my.TButton", font=("Arial",16,"bold"))
button1 = ttk.Button(menu, text ="click now", style="my.TButton")
button1.pack(fill="x" ,side="left")
button2 = ttk.Button(menu, text = "place holder" , style="my.TButton") 
button2.pack(fill="x",)

root.mainloop()

