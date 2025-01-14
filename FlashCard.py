from tkinter import *
import pandas
import random
current_card={}
BACKGROUND_COLOR = "#B1DDC6"
to_learn={}
try:
    data=pandas.read_csv("word_to_learn.csv")
except FileNotFoundError:
    org_data=pandas.read_csv("french - Sheet1.csv")
    to_learn=org_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
def next_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_bg,image=card_front_image)
    flip_timer=window.after(3000,func=flip_card)
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_bg,image=card_back_image )
def is_known():
    global current_card
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("word_to_learn.csv",index=False)
    next_word()

window=Tk()
window.title("Flash Card")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
card_front_image=PhotoImage(file="card_front.png")
card_back_image=PhotoImage(file="card_back.png")
card_bg=canvas.create_image(400,263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_word=canvas.create_text(400,260, text="Word", font=("Arial",40,"bold"))
card_title=canvas.create_text(400,150, text="Title", font=("Arial",40,"italic"))
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="wrong.png")
cross_button=Button(image=cross_image,command=next_word)
cross_button.grid(row=1, column=0)

yes_image=PhotoImage(file="right.png")
yes_button=Button(image=yes_image,command=is_known)
yes_button.grid(row=1, column=1)

next_word()


window.mainloop()
