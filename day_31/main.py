from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

with open("am_en.csv", "r") as french_word:
    data = pandas.read_csv(french_word)
    word_in_dict = {row.English: row.Amharic for (index, row) in data.iterrows()}

list_english = list(word_in_dict)
english_word = ""

def delete_word_from_file(word):
    print(f"delete: {word}")
    del word_in_dict[word]
    start_learning()


def pick_word():
    english_word = random.choice(list_english)
    french_word = word_in_dict[english_word]
    return english_word, french_word


window = Tk()
window.title("Learn French")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
card_front_photo = PhotoImage(file="images/card_front.png")
card_back_photo = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=600, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
v_photo = PhotoImage(file="images/right.png")
x_photo = PhotoImage(file="images/wrong.png")


# front card
def front_design():
    canvas.create_image(350, 100, image=card_front_photo)
    canvas.grid(column=0, row=0, columnspan=5, rowspan=4)


# back card
def back_design():
    canvas.create_image(350, 100, image=card_back_photo)
    canvas.grid(column=0, row=0, columnspan=5, rowspan=4)


# english_label
def langughi_design(english_or_french, bg_color):
    english_labe = Label(text=english_or_french)
    english_labe.config(font=("Arial", 20, "italic"), bg=bg_color, width=10)
    english_labe.grid(column=2, row=0)


# translated word
def translating_word_design(word, bg_color):
    translated_label = Label(text=word)
    translated_label.config(font=("Arial", 40), bg=bg_color, width=10, height=3)
    translated_label.grid(column=2, row=1)


def start_translate(english_word):
    back_design()
    langughi_design("English", BACKGROUND_COLOR)
    translating_word_design(english_word, BACKGROUND_COLOR)


def start_learning():
    global english_word
    front_design()
    english_word, french_word = pick_word()
    langughi_design("French", "white")
    translating_word_design(french_word, "white")
    window.after(5000, start_translate, english_word)


#  x label
x_photo_label = Button(image=x_photo, width=100, height=100, bg=BACKGROUND_COLOR, highlightthickness=0,
                       command=start_learning)
x_photo_label.grid(column=1, row=3)

# y label
v_photo_label = Button(image=v_photo, width=100, height=100, bg=BACKGROUND_COLOR, highlightthickness=0,
                       command=lambda: delete_word_from_file(english_word))
v_photo_label.grid(column=3, row=3)

start_learning()

window.mainloop()
