import requests
from datetime import datetime


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print the status of the code (number)
# print(response.status_code)
# print what error we got
# response.raise_for_status()
# get the data inside this api
# latitude = response.json()["iss_position"]["latitude"]
# longitude = response.json()["iss_position"]["longitude"]
#
# iss_postion = (longitude, latitude)
# print(iss_postion)
my_lat = 31.761834
my_lng = 35.216492
parameters = {
    "lat":my_lat,
    "lng":my_lng,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.now()
hour_now = time_now.hour

print(f"the sunrise: {sunrise}")
print(f"the susnset: {sunset}")
print(f"the time now: {hour_now}")

