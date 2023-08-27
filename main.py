import math
from tkinter import *

## CREDITS TO Dr. Angela Yu for this idea from her 100 days of python course.


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier New"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
image_path = "tomato2.png"
time_intervals_completed = 0
previous_session = None
fg = GREEN

checkmark_list = []
timer = None
is_loop_finished = -1  # Indicates whether a Work session countdown has finished


def reset():
    """
    Resets the window to initial values

    :return:
    """
    global timer
    window.after_cancel(timer)
    global time_intervals_completed
    global checkmark_list
    time_intervals_completed = 0
    canvas.itemconfig(time_text, text=f"00:00")
    label.config(text="Pomodoro", fg=GREEN)
    start_button.config(text="Start")

    checkmark_list = []
    checkmark.config(text="")


def start_timer():
    """
    Starts the timer and updates the screen.
    :return:
    """
    global time_intervals_completed
    global is_loop_finished
    global timer
    global previous_session
    global checkmark_list

    # Cancel any running timers
    if time_intervals_completed > 0:
        window.after_cancel(timer)

    # If user finished early in their Work session, update the checkmark indicating completion.
    if previous_session == "Work" and is_loop_finished == 0:
        add_checkmark()
        is_loop_finished = 1  # Reset indicator

    # If user finishes 4 Work sessions then reset tickmark count
    if len(checkmark_list) == 4:
        checkmark_list = []
        checkmark.config(text="")

    seconds_to_work = {"work": WORK_MIN * 60, "break": SHORT_BREAK_MIN * 60, "long_break": LONG_BREAK_MIN * 60}

    # Update UI according to the "Long Break" session parameters.
    if time_intervals_completed % 7 == 0 and time_intervals_completed != 0:
        label.config(text="Long Break", fg=PINK)
        count_down(seconds_to_work["long_break"])
        start_button.config(text="Start\nWork")
        previous_session = "Long Break"
        time_intervals_completed += 1

    # Update UI according to the "Work" session parameters.
    elif time_intervals_completed % 2 == 0:
        label.config(text="Work", fg=GREEN)
        previous_session = "Work"
        count_down(seconds_to_work["work"])
        start_button.config(text="Start\nBreak")
        time_intervals_completed += 1

    # Update UI according to the "Break" session parameters.
    elif time_intervals_completed % 2 == 1:
        label.config(text="Break", fg=RED)
        count_down(seconds_to_work["break"])
        start_button.config(text="Start\nWork")
        previous_session = "Break"
        time_intervals_completed += 1


def count_down(count):
    """
    Sets a countdown from 'count' value to zero.

    :param count: Number of seconds
    :return:
    """
    global timer
    global is_loop_finished

    # Bring text in MM:SS format
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

    # Update screen with latest time
    canvas.itemconfig(time_text, text=f"{minutes_text}:{seconds_text}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # Recall function after one second
    is_loop_finished = 0

    # Add checkmark on screen if a Work session is finished
    if count == 0 and time_intervals_completed % 2 != 0:
        add_checkmark()
        is_loop_finished = 1


def add_checkmark():
    """
    Adds a tick mark to the 'checkmark' list.
    :return:
    """
    global checkmark_list
    if len(checkmark_list) == 4:
        checkmark_list = []
    checkmark_list.append("🗸")
    checkmarks_string = "".join(checkmark_list)  # Convert list to string
    checkmark.config(text=checkmarks_string)


# Create a Tkinter Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=50, bg=YELLOW)

# Create Canvas for background image

canvas = Canvas(width=275, height=400, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_path)
canvas.create_image(150, 250, image=tomato_img)

# Add timer text and buttons
time_text = canvas.create_text(140, 250, text="00:00", fill="black", font=("Calibri", 27, "bold"))
label = Label(text="Pomodoro", bg=YELLOW, fg=fg, font=(FONT_NAME, 30, "bold"))
start_button = Button(master=window, text="Start", command=start_timer, font=("helvetica", 12, "bold"), bd=0, bg=GREEN,
                      fg=YELLOW, padx=5, pady=5)
reset_button = Button(master=window, text="Reset", command=reset, font=("helvetica", 12, "bold"), bd=0, bg=GREEN,
                      fg=YELLOW, padx=5, pady=5)

# Place all widgets in respective grids
label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=3)

checkmark = Label(text="", bg=YELLOW, fg=fg, font=("Courier", 35, "bold"))
checkmark.grid(row=3, column=1)

window.mainloop()
