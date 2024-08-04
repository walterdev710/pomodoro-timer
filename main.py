from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    
    # change title_label
    timer_label.config(text="Timer", fg=GREEN)
    # reset the check mark
    check_mark_label.config(text="")
    
    # reset the clock
    canvas.itemconfigure(time_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():    
    global reps
    reps += 1
    
    work_minute = WORK_MIN * 60
    short_break_minute = SHORT_BREAK_MIN * 60
    long_break_minute = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_minute)
        timer_label.configure(text="Long Break", fg=PINK,font=(FONT_NAME, 30, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_minute)
        timer_label.configure(text="Break", fg=RED, font=(FONT_NAME, 35, "bold"))      
    else:
        count_down(work_minute)
        timer_label.configure(text="Work", font=(FONT_NAME, 35, "bold"))
        
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    
    
    canvas.itemconfigure(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks =""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks +="✔️"
        check_mark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #   
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

time_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 28,"bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start",highlightthickness=0, bg="white", command=start_timer)
start_btn.grid(column=0, row=2)

check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_mark_label.grid(row=3, column=1)

reset_btn = Button(text="Reset", highlightthickness=0,bg="white", command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()