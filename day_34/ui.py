import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"





class QuizzInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Naama's Trivia")
        self.window.configure(pady= 30, padx= 30, bg=THEME_COLOR)
        self.question = Canvas(bg="white", height=250, width= 300)
        self.question_text = self.question.create_text(150, 125, width=250, text="", fill=THEME_COLOR, font=("Ariel", 15, "bold"))
        self.question.grid(column=1, row=2, columnspan =3)
        true_photo = PhotoImage(file="/home/shay/snake_game/udimy/day_34/images/true.png")
        self.true_button = Button(image= true_photo, command=self.true_button)
        self.true_button.grid(column=1, row= 4)
        false_photo = PhotoImage(file="/home/shay/snake_game/udimy/day_34/images/false.png")
        self.false_button = Button(image= false_photo, command= self.false_button)
        self.false_button.grid(column=3, row= 4, padx= 20, pady = 20)
        self.score_label = Label(text="score: 0", fg="white", font=("Ariel", 15, "bold"), bg=THEME_COLOR)
        self.score_label.grid(row= 0, column= 3)
        self.get_new_q()


        self.window.mainloop()


    def get_new_q(self):
        self.question.config(bg="white")
        if self.quiz.still_has_questions():
            self.quiz.question_number += 1
            text_q = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text= text_q)
        else:
            self.question.itemconfig(self.question_text, text=f"End of game!\n")
            self.false_button.config(state= "disabled")
            self.true_button.config(state= "disabled")

    def change_window_background(self, answer):
        if answer:
            self.question.config(bg="green")
        else:
            self.question.config(bg="red")
        self.window.after(1000, self.get_new_q)



    def true_button(self):
        answer = self.quiz.check_answer("True")
        self.score_label.config(text=f"score: {self.quiz.score}")
        self.change_window_background(answer)


    def false_button(self):
        answer = self.quiz.check_answer("False")
        self.score_label.config(text=f"score: {self.quiz.score}")
        self.change_window_background(answer)


    def end_game(self):
        self.question_text = self.question.create_text(150, 125, width=250, text=f"Your current score is: {self.quiz.score}/{self.quiz.question_number}", fill=THEME_COLOR, font=("Ariel", 15, "bold"))
        self.question.grid(column=1, row=2, columnspan =3)
        exit(0)











