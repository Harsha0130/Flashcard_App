from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#70d8e3"

# ---------------------------- CREATING NEW FLASH CARDS ------------------------------- #
data = pandas.read_csv("data/kannada_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)


def start():
    next_card()
    start_button.destroy()


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="Kannada")
    canvas.itemconfig(word_text, text=current_card["Kannada"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashh")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

yes_image = PhotoImage(file="images/yes.png")
yes_button = Button(image=yes_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground="#00fd00",
                    command=next_card)
yes_button.grid(column=0, row=1, padx=20, pady=20)

no_image = PhotoImage(file="images/no.png")
no_button = Button(image=no_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground="#ff0000",
                   command=next_card)
no_button.grid(column=1, row=1, padx=20, pady=20)

start_button = Button(text="Start", highlightthickness=0, width=15, activebackground=BACKGROUND_COLOR, height=5,
                      font=("Ariel", 30, "bold"), command=start)
start_button.grid(column=0, row=0, columnspan=2)

window.mainloop()
