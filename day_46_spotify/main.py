import requests
from bs4 import BeautifulSoup

# date = input("please enter a date that you wanna listen to(formate: YYYY-MM-DD): ")
URL = "https://www.billboard.com/charts/hot-100/2000-08-22/"

response = requests.get(URL)
response = response.text
soup = BeautifulSoup(response, "html.parser")
all_songs_data = soup.find("h3", class_=".c-title")
print(all_songs_data)
nice = all_songs_data.string


