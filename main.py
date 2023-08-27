import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier New"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
image_path = "tomato2.png"
time_intervals_completed = 0
last_session = None

checkmark = []
timer = None
loop_finish = -1


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer
    window.after_cancel(timer)
    global time_intervals_completed
    global checkmark
    time_intervals_completed = 0
    canvas.itemconfig(time_text, text=f"00:00")
    label.config(text="Pomodoro", fg=GREEN)
    start_button.config(text="Start")

    checkmark = []
    print_checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global time_intervals_completed
    global loop_finish
    global timer
    global last_session
    global checkmark
    if time_intervals_completed > 0:
        window.after_cancel(timer)

    if last_session == "Work" and loop_finish == 0:
        add_checkmark()
        loop_finish = 1
    if len(checkmark) == 4:
        checkmark = []
        print_checkmark.config(text="")
    seconds_to_work = {"work": WORK_MIN * 60, "break": SHORT_BREAK_MIN * 60, "long_break": LONG_BREAK_MIN * 60}
    if time_intervals_completed % 7 == 0 and time_intervals_completed != 0:
        label.config(text="Long Break", fg=PINK)
        count_down(seconds_to_work["long_break"])
        start_button.config(text="Start\nWork")
        last_session = "Long Break"
        time_intervals_completed += 1

    elif time_intervals_completed % 2 == 0:
        label.config(text="Work", fg=GREEN)
        last_session = "Work"
        count_down(seconds_to_work["work"])
        start_button.config(text="Start\nBreak")

        time_intervals_completed += 1

    elif time_intervals_completed % 2 == 1:
        label.config(text="Break", fg=RED)
        count_down(seconds_to_work["break"])
        start_button.config(text="Start\nWork")
        last_session = "Break"

        time_intervals_completed += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    global loop_finish
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
        timer = window.after(1000, count_down, count - 1)
    loop_finish = 0
    if count == 0 and time_intervals_completed % 2 != 0:
        add_checkmark()
        loop_finish = 1


def add_checkmark():
    global checkmark
    if len(checkmark) == 4:
        checkmark = []
    checkmark.append("🗸")
    checkmarks_string = "".join(checkmark)
    print_checkmark.config(text=checkmarks_string)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=50, bg=YELLOW)
fg = GREEN
canvas = Canvas(width=275, height=400, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_path)
canvas.create_image(150, 250, image=tomato_img)
time_text = canvas.create_text(140, 250, text="00:00", fill="black", font=("Calibri", 27, "bold"))
label = Label(text="Pomodoro", bg=YELLOW, fg=fg, font=(FONT_NAME, 30, "bold"))
start_button = Button(master=window, text="Start", command=start_timer, font=("helvetica", 12, "bold"), bd=0, bg=GREEN,
                      fg=YELLOW, padx=5, pady=5)
reset_button = Button(master=window, text="Reset", command=reset, font=("helvetica", 12, "bold"), bd=0, bg=GREEN,
                      fg=YELLOW, padx=5, pady=5)
label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=3)
print_checkmark = Label(text="", bg=YELLOW, fg=fg, font=("Courier", 35, "bold"))
print_checkmark.grid(row=3, column=1)

window.mainloop()
