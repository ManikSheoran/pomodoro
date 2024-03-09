from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#f862cb"
RED = "#e7305b"
GREEN = "#259645"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps, timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label.config(text="TIMER", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_counter():
    global reps
    if reps % 2 == 0 and (reps + 1) % 8 != 0:
        time = WORK_MIN * 60
        check.config(text=f"🔥 {int(reps / 2)}", bg=YELLOW, font="bold")
        label.config(text="WORK TIMER", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
    elif reps % 2 == 1 and (reps + 1) % 8 != 0:
        time = SHORT_BREAK_MIN * 60
        check.config(text=f"🔥 {int(reps / 2)}", bg=YELLOW, font="bold")
        label.config(text="SHORT BREAK", fg=PINK, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
    else:
        time = LONG_BREAK_MIN * 60
        check.config(text=f"🔥 {int(reps / 2)}", bg=YELLOW, font="bold")
        label.config(text="LONG BREAK", fg=RED, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
    reps += 1
    counter(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, counter, count - 1)
    else:
        start_counter()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.config(bg=YELLOW, padx=50, pady=50)
canvas = Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="download.png")
canvas.create_image(150, 112, image=tomato)
timer_text = canvas.create_text(150, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
label.grid(column=1, row=0)


def action1():
    if reps == 0:
        start_counter()
    else:
        None


start = Button(text="START", command=action1)
start.grid(column=0, row=2)

reset = Button(text="RESET", command=reset)
reset.grid(column=2, row=2)

check = Label(text="", fg=RED, bg=YELLOW, font="bold")
check.grid(column=1, row=3)

window.mainloop()
