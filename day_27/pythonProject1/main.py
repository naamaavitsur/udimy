from tkinter import *

window = Tk()
window.title("naama GUI")
window.minsize(600, 600)
my_label = Label(text="I am text", font=("Ariel", 24, "bold"))
my_label.config(text="cool!")
my_label.grid(column= 0, row= 0)

def buttom_clicked():
    hey = input.get()
    my_label.config(text=hey)

buttom = Button(text="click", command=buttom_clicked)
buttom.grid(column= 1, row= 1)

new_button = Button(text= "new")
new_button.grid(column= 2, row= 0)

input = Entry(width=10, )
input.grid(column= 3, row= 2)






window.mainloop()

# def add(*args):
#     answer = 0
#     for i in args:
#         answer += i
#     return answer
#
#
# print(add(1,2,3,5,8))

