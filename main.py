import math
import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
image_path = "tomato.png"
time_intervals_completed = 0
work_sessions_completed = 0
checkmark = []


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global time_intervals_completed
    global work_sessions_completed
    seconds_to_work = {"work": 2 * 1, "break": 2 * 1, "long_break": 10 * 1}
    if time_intervals_completed % 7 == 0 and time_intervals_completed != 0:
        label.config(text="Long Break")
        count_down(seconds_to_work["long_break"])
        start_button.config(text="Start Work")
        time_intervals_completed += 1

    elif time_intervals_completed % 2 == 0:
        label.config(text="Work")
        count_down(seconds_to_work["work"])
        start_button.config(text="Start Break")
        time_intervals_completed += 1
        work_sessions_completed += 1
    elif time_intervals_completed % 2 == 1:
        label.config(text="Break")
        count_down(seconds_to_work["break"])
        start_button.config(text="Start Work")
        time_intervals_completed += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes_text = math.floor(count / 60)
    seconds_text = round(count % 60)
    if seconds_text == 0:
        seconds_text = "00"
    elif seconds_text < 10:
        seconds_text = f"0{seconds_text}"
    if minutes_text == 0:
        minutes_text = "00"
    elif minutes_text < 10:
        minutes_text = f"0{minutes_text}"

    canvas.itemconfig(time_text, text=f"{minutes_text}:{seconds_text}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    if count == 0 and time_intervals_completed % 2 != 0:
        add_checkmark()


def add_checkmark():
    global checkmark
    checkmark.append("🗸")
    checkmarks_string = "".join(checkmark)
    print_checkmark.config(text=checkmarks_string)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
fg = GREEN
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
label = Label(text="Pomodoro", bg=YELLOW, fg=fg, font=(FONT_NAME, 30, "bold"))
start_button = Button(master=window, text="Start", command=start_timer)
reset_button = Button(master=window, text="Reset")
label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=3, column=0)
reset_button.grid(row=3, column=3)
print_checkmark = Label(text="", bg=YELLOW, fg=fg, font=(FONT_NAME, 25, "bold"))
print_checkmark.grid(row=2, column=1)

window.mainloop()
