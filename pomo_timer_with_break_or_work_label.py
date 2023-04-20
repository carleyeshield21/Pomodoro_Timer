from tkinter import *
# We import the math module for the rounding off the numbers for the timer display, we can use the math.floor to truncate the decimal places in the division without altering the whole number
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
style = 'Goudy Old Style'
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def is_start_count():
    # This function needs to be called in the else statement of the count_down function when count reaches zero
    global reps
    reps += 1

    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    print(reps)

    if reps %  8 == 0:
        count_down(long_break_sec)
        timer_title.config(text="Long Break",foreground=RED)
    elif reps %  2 == 0:
        count_down(short_break_sec)
        timer_title.config(text="Short Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_title.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Here, we have used the feature in Python called Dynamic Typing to achieve the desired format of the timer
    # display, a combination of integers and strings in a single output display
    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f'0{minutes}'

    if seconds < 10:
        seconds = f'0{seconds}'

    # using itemconfig to change the text in the timer to the actual timer
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        # print(count)
        window.after(1000,count_down,count-1)
    else:
        is_start_count()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro's Tomato")
# This code sets the background color and the dimensions for the window created in tkinter
window.config(padx=100,pady=50,bg=YELLOW)
# We must call the function count_down after the canvas for it to execute
# count_down(10)

# The line of code with the highlight thickness set to zero to even out the border between to backgrounds
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# canvas = Canvas(width=200,height=224,bg=YELLOW)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 100, image=tomato_img)
# This code sets the background color of the canvas photo file
timer_text = canvas.create_text(100, 124, text='Poteto',fill='blue',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)
# count_down(10)

timer_title = Label(text='Tay-mer',font=('Comic Sans MS',50,'bold'),highlightthickness=0,background=YELLOW)
timer_title.grid(row=0,column=1)

start_button = Button(text='Is-start',font=("Regular",25,'bold'),command=is_start_count)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset',font=("Regular",25,'bold'),highlightthickness=0)
reset_button.grid(row=2,column=2)

chick_mark = Label(text='✅',foreground=RED,background=GREEN,font=('Regular',25),highlightthickness=0)
chick_mark.grid(row=3,column=1)

pomo_reps = Entry(width=5)
pomo_reps.grid(row=0,column=0)


window.mainloop()