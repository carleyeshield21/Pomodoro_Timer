from tkinter import *
from tkinter import font
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
style = 'Goudy Old Style'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro's Tomato")
# This code sets the background color and the dimensions for the window created in tkinter
window.config(padx=100,pady=50,bg=YELLOW)

# The line of code with the highlight thickness set to zero to even out the border between to backgrounds
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# canvas = Canvas(width=200,height=224,bg=YELLOW)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 100, image=tomato_img)
# This code sets the background color of the canvas photo file
canvas.create_text(100, 124, text='Poteto',fill='blue',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)
# canvas.pack()

# timer_title = Label(text='Tay-mer',font=(style,50,'bold'))
timer_title = Label(text='Tay-mer',font=('Comic Sans MS',50,'bold'),highlightthickness=0,background=YELLOW)
timer_title.grid(row=0,column=1)

start_button = Button(text='Is-start',font=("Regular",25,'bold'))
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset',font=("Regular",25,'bold'),highlightthickness=0      )
reset_button.grid(row=2,column=2)

chick_mark = Label(text='✅',foreground=RED,background=GREEN,font=('Regular',25),highlightthickness=0)
chick_mark.grid(row=3,column=1)

window.mainloop()