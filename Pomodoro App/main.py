from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
timer_running = False
paused = False  
remaining_time = 0  
def reset_timer():
    global timer_running, paused, reps, remaining_time
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0
    timer_running = False
    paused = False
    remaining_time = 0

def start_timer():
    global reps, timer_running, paused, remaining_time
    
    if timer_running and not paused: 
        return
    
    if paused and remaining_time > 0: 
        count_down(remaining_time)
        paused = False
    else:
        timer_running = True
        reps += 1 
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            title_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text="Break", fg=PINK)
        else:
            count_down(work_sec)
            title_label.config(text="Work", fg=GREEN)

    timer_running = True

def pause_timer():
    global paused, remaining_time, timer
    if timer_running and not paused: 
        paused = True
        window.after_cancel(timer) 
        current_time = canvas.itemcget(timer_text, "text")
        minutes, seconds = map(int, current_time.split(":"))
        remaining_time = minutes * 60 + seconds 

def count_down(count):
    global timer, remaining_time
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
        remaining_time = count 
    else:
        global timer_running
        timer_running = False
        start_timer()  
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg="Green", font=(FONT_NAME, 50), highlightthickness=0, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro App/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", highlightthickness=0, bd=0, borderwidth=0, command=start_timer)
start_button.grid(column=0, row=2)

pause_button = Button(text="Pause", highlightthickness=0, bd=0, borderwidth=0, command=pause_timer)
pause_button.grid(column=1, row=2) 

reset_button = Button(text="Reset", highlightthickness=0, bd=0, borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
check_marks.grid(column=1, row=3)

window.mainloop()
