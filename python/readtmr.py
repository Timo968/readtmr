import time
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

def save_progress(title, current_page, total_pages, time_per_page):
    with open("reading_progress.txt", "w") as file:
        file.write(f"{title}\n{current_page}\n{total_pages}\n{time_per_page}")

def load_progress():
    if os.path.exists("reading_progress.txt"):
        with open("reading_progress.txt", "r") as file:
            title = file.readline().strip()
            current_page = int(file.readline().strip())
            total_pages = int(file.readline().strip())
            time_per_page = float(file.readline().strip())
        return title, current_page, total_pages, time_per_page
    else:
        return None

def start_countdown():
    start_time = time.time()

    finished_page = simpledialog.askinteger("Finished Page", "Which page did you finish reading?")
    elapsed_time = time.time() - start_time

    if current_page.get() != finished_page:
        time_per_page.set((time_per_page.get() * current_page.get() + elapsed_time) / finished_page)

    save_progress(title.get(), finished_page, total_pages.get(), time_per_page.get())

    remaining_pages = total_pages.get() - finished_page
    remaining_time = remaining_pages * time_per_page.get()

    hours, remainder = divmod(remaining_time, 3600)
    minutes = remainder // 60

    messagebox.showinfo("Remaining Time", f"You will need approximately {int(hours)} hours and {int(minutes)} minutes to finish the book.")

progress = load_progress()

root = tk.Tk()
root.title("Reading Progress Tracker")

title = tk.StringVar()
current_page = tk.IntVar()
total_pages = tk.IntVar()
time_per_page = tk.DoubleVar()

if progress:
    title.set(progress[0])
    current_page.set(progress[1])
    total_pages.set(progress[2])
    time_per_page.set(progress[3])
else:
    title.set("testbook")
    current_page.set(0)
    total_pages.set(100)
    time_per_page.set(0)

title_label = tk.Label(root, text="Book Title:")
title_label.grid(row=0, column=0, sticky="e")
title_entry = tk.Entry(root, textvariable=title)
title_entry.grid(row=0, column=1)

total_pages_label = tk.Label(root, text="Total Pages:")
total_pages_label.grid(row=1, column=0, sticky="e")
total_pages_entry = tk.Entry(root, textvariable=total_pages)
total_pages_entry.grid(row=1, column=1)

start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
