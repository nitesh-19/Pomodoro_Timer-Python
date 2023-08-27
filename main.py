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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
fg = GREEN
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))

label = Label(text="Timer", bg=YELLOW, fg=fg, font=(FONT_NAME, 30, "bold"))
sessions_completed = 2
checkmarks = ["🗸" for i in range(0, sessions_completed)]
checkmarks_string = "".join(checkmarks)
print_checkmark = Label(text=checkmarks_string, bg=YELLOW, fg=fg, font=(FONT_NAME, 25, "bold"))
start_button = Button(master=window, text="Start")
reset_button = Button(master=window, text="Reset")

label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
print_checkmark.grid(row=2, column=1)
start_button.grid(row=3, column=0)
reset_button.grid(row=3, column=3)
window.mainloop()
