import time
import os

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

progress = load_progress()

if progress:
    title, current_page, total_pages, time_per_page = progress
else:
    title = input("What book are you reading? ")
    if title == "":
        title = "testbook"
        print("testvariable: testbook")

    total_pages = input("How many pages are in the book? ")
    if total_pages == "":
        total_pages = 100
        print("testvariable: 100")
    else:
        total_pages = int(total_pages)

    current_page = 0
    time_per_page = 0

input("Press any key to start the countdown.")
start_time = time.time()

finished_page = int(input("Which page did you finish reading? "))
elapsed_time = time.time() - start_time

if current_page != finished_page:
    time_per_page = (time_per_page * current_page + elapsed_time) / finished_page

save_progress(title, finished_page, total_pages, time_per_page)

remaining_pages = total_pages - finished_page
remaining_time = remaining_pages * time_per_page

hours, remainder = divmod(remaining_time, 3600)
minutes = remainder // 60

print(f"You will need approximately {int(hours)} hours and {int(minutes)} minutes to finish the book.")

