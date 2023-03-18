import tkinter
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
reps = 0
timer = None
mark = ''
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text='Timer', font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
    mark1.config(text=mark)
    canvas.itemconfig(count_dn_screen, text='00:00')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    minutes_work = WORK_MIN * 60
    minutes_short = SHORT_BREAK_MIN * 60
    minutes_long = LONG_BREAK_MIN * 60

    if reps in [1, 3, 5, 7]:
        label.config(text='WORK', font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
        count_down(minutes_work)
    elif reps == 8:
        label.config(text='BREAK', font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)
        count_down(minutes_long)
    else:
        label.config(text='STOP', font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED)
        count_down(minutes_short)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

        count_minute = math.floor(count / 60)
        count_second = count % 60
        if count_second < 10:
            count_second = f"0{count_second}"

        canvas.itemconfig(count_dn_screen, text=f'{count_minute}:{count_second}')
        if count > 0:
            global timer
            timer = window.after(1000, count_down, count-1)
        else:
            start_timer()
            global mark
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                mark += '✓'
            mark1.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
#window
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


#label_time
label = tkinter.Label(text='Timer', font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=1)
mark1 = tkinter.Label(font=('', 30), fg=GREEN, bg=YELLOW)
mark1.grid(column=1, row=4)


#background image
canvas = tkinter.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato_img)
count_dn_screen = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

#BUTTON
start_b = tkinter.Button(text='Start', bg='white', width=3, command=start_timer)
reset_b = tkinter.Button(text='Reset', bg='white', width=3, command=reset_timer)
start_b.grid(column=0, row=3)
reset_b.grid(column=2, row=3)







window.mainloop()