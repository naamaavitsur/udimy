# things to remember:
# cd- go to place - cd name you want to enter to. if you want to go back to write ".."
# ls - see what inside the dire
# pwd - print working directory
# touch - make new file
# mkdir - make new dire
# rm - delete file
#( rm - rf ) - delete dire- delete everything inside
from flask import Flask
app = Flask(__name__)




def make_bolt_decorator(func):
    def inner_func():
        return "<b>" + func() + "</b>"
    return inner_func


@app.route("/")
@make_bolt_decorator
def hello_world():
    return "Hello, World!"


@app.route("/naama")
def cool_naama():
    return "naama so cool"


if __name__ == '__main__':
    app.run(debug=True)
#
#
# def delay_decoratoe(function):
#     def second():
#         time.sleep(2)
#         function()
#         time.sleep(2)
#         function()
#     return second()
#
# @delay_decoratoe
# def print():
#     print("yay")


import time

# current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970


# def speed_calc_decorator(function):
#     def inner_func():
#         befor_time = time.time()
#         function()
#         after_time = time.time()
#         runing_lengh = after_time - befor_time
#         print(f"the func: {function.__name__}, run : {runing_lengh}")
#     return inner_func()
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i



