from datetime import datetime
import requests

API_KEY = "66999113e478bc886459a0beb3b27c12"
API_ID = "125d0a62"
HOST_DOMAIN = "https://trackapi.nutritionix.com"
API_END_PONT_BURNED = "/v2/natural/exercise"
API_END_PONT_FOOD = "/v2/search/instant"

API_END_POINT_SHEET = "עותק של My Workouts"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}


workout_input = input("What exersice you did today?: ")

parameter= {"query": workout_input,
            "weight_kg": "52",
            "height_cm": "162",
            "age": "34"}

response = requests.post(f"{HOST_DOMAIN}{API_END_PONT_BURNED}", headers=headers, json=parameter)
exercise_response = response.json()["exercises"]
date = datetime.now().strftime("%d.%m.%Y")
for i in exercise_response:
    params = {
        "workout": {
            "date": date,
            "time": f"{datetime.now().hour}:{datetime.now().minute}",
                "exercise" : i["user_input"],
                "duration": i["duration_min"],
                "calories": i["nf_calories"]}}
    sheets_response = requests.post(url="https://api.sheety.co/568d87cc33651c639e80928b873010f3/myWorkouts/workouts", auth=("naamaavitsur", "98765432"), json=params)
    print(sheets_response.text)


# list_of_workout_lists = []
# exercise_type = ["run", "swim", "cycle", "walk"]
# list_of_workout_input = workout_input.split()
# for i in list_of_workout_input:
#     if i in exercise_type:
#         list_of_one_workout = []
#         list_of_one_workout.append(i)
#         index = list_of_workout_input.index(i)
#         checked_word_if_number = list_of_workout_input[index+1]
#         if checked_word_if_number.isdigit():
#             list_of_one_workout.append(checked_word_if_number)
#             list_of_one_workout.append(list_of_workout_input[index+2])
#             calory_burned = int(checked_word_if_number) * 50
#             list_of_one_workout.append(calory_burned)
#         date = datetime.now()
#         date = date.strftime("%d.%m.%Y")
#         list_of_one_workout.append(date)
#         list_of_workout_lists.append(list_of_one_workout)
# print(list_of_workout_lists)



