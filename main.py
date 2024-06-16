from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#70d8e3"
current_card = {}
to_learn = {}

# ---------------------------- CREATING NEW FLASH CARDS ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("kannada_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="Kannada", fill="black")
    canvas.itemconfig(word_text, text=current_card["Kannada"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIPPING THE CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


# ---------------------------- FLIPPING THE CARD ------------------------------- #
def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashh")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

yes_image = PhotoImage(file="images/yes.png")
yes_button = Button(image=yes_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground="#00fd00",
                    command=is_known)
yes_button.grid(column=1, row=1, padx=20, pady=20)

no_image = PhotoImage(file="images/no.png")
no_button = Button(image=no_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground="#ff0000",
                   command=next_card)
no_button.grid(column=0, row=1, padx=20, pady=20)

next_card()

window.mainloop()
