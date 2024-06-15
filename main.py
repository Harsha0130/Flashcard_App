from tkinter import *
BACKGROUND_COLOR = "#70d8e3"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashh")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="Kannada", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="yenu", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

yes_image = PhotoImage(file="images/yes.png")
yes_button = Button(image=yes_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground="#00fd00")
yes_button.grid(column=0, row=1, padx=20, pady=20)

no_image = PhotoImage(file="images/no.png")
no_button = Button(image=no_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground="#ff0000")
no_button.grid(column=1, row=1, padx=20, pady=20)


window.mainloop()
