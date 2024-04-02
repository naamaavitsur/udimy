from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK_MARKS = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, check_marks, timer, CHECK_MARKS
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(count_down_text, text="00:00")
    reps = 0
    CHECK_MARKS = ""
    check_marks.config(text=CHECK_MARKS, bg=YELLOW, fg=GREEN, font=("bold", 30))



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps , timer
    global CHECK_MARKS

    reps += 1
    if reps % 8 == 0:
        CHECK_MARKS += "✓"
        check_marks.config(text=CHECK_MARKS, bg=YELLOW, fg=GREEN, font=("bold", 30))
        timer_label.config(text="Long Break", fg=PINK, bg= YELLOW, font=("bold", 30))
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 1:
        timer_label.config(text="Work Time", fg=RED, bg=YELLOW, font=("bold", 30))
        count_down(WORK_MIN)
    elif reps % 2 == 0:
        CHECK_MARKS += "✓"
        check_marks.config(text=CHECK_MARKS, bg=YELLOW, fg=GREEN, font=("bold", 30))
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW, font=("bold", 30))
        count_down(SHORT_BREAK_MIN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    minute = math.floor(count/60)
    second = count % 60
    if second == 0:
        second = "00"
    elif second < 10:
        second = f"0{second}"
    canvas.itemconfig(count_down_text, text=f"{minute}:{second}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        window.after(1000, start_timer)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("עגבניה")
window.config(pady=100, padx=150, bg= YELLOW)
tomato_photo = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 100, image=tomato_photo)
count_down_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column= 1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("bold", 30))
timer_label.grid(row=0, column=1)

reset_button = Button(text="Reset", bg=PINK, font=FONT_NAME, width=3, highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

check_marks = Label(bg=YELLOW, fg=GREEN, font=("bold", 30))
check_marks.grid(row=3, column=1)

start_button = Button(text="Start", bg=PINK, font=FONT_NAME, width=3, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)



window.mainloop()