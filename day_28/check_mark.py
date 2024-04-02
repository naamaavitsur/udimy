from tkinter import Canvas

class CheckMark():
    def __init__(self):
        check_mark = PhotoImage(file="Antu_games-endturn.svg.png")
        self.check_mark = Canvas(width=10, height=10, bg=YELLOW, highlightthickness=0)
        self.check_mark.create_image(100, 100, image=check_mark)

