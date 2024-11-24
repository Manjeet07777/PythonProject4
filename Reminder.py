import tkinter as tk
from tkinter import messagebox
import time
import threading

def set_reminder():
    reminder_time = time_entry.get()  
    message = message_entry.get() 
    if not reminder_time or not message:
        messagebox.showwarning("Input Error", "Please enter both time and message!")
        return
    
    try:
       
        hours, minutes = map(int, reminder_time.split(":"))
        total_seconds = hours * 3600 + minutes * 60

       
        current_time = time.localtime()
        current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
        delay = total_seconds - current_seconds

        if delay < 0:
            messagebox.showwarning("Time Error", "The time has already passed!")
            return
        
       
        threading.Thread(target=show_alert, args=(delay, message), daemon=True).start()
        messagebox.showinfo("Reminder Set", f"Reminder set for {reminder_time}!")
    except ValueError:
        messagebox.showerror("Format Error", "Please enter time in HH:MM format.")


def show_alert(delay, message):
    time.sleep(delay)
    messagebox.showinfo("Reminder Alert", message)


root = tk.Tk()
root.title("Reminder Application")


title_label = tk.Label(root, text="Reminder Application", font=("Arial", 16, "bold"))
title_label.pack(pady=10)


time_label = tk.Label(root, text="Enter Time (HH:MM):", font=("Arial", 12))
time_label.pack(pady=5)
time_entry = tk.Entry(root, font=("Arial", 12), width=10)
time_entry.pack(pady=5)


message_label = tk.Label(root, text="Enter Reminder Message:", font=("Arial", 12))
message_label.pack(pady=5)
message_entry = tk.Entry(root, font=("Arial", 12), width=30)
message_entry.pack(pady=5)


set_button = tk.Button(root, text="Set Reminder", font=("Arial", 12), command=set_reminder)
set_button.pack(pady=20)

root.mainloop()
