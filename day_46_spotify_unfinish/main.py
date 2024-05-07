import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_id = "3144ihsdwqf5cqeqit3ogtohc5pu"
client_id = "b35ea8ba3ea14ba7b77efbcfa4d7cf0f"
client_secret = "12f55198e7de4d49b7c535d2dd08442b"

url_get_token = "/api/token"
URL_BILIBOARD = "https://www.billboard.com/charts/hot-100/"
URL_ENDPOINT = "https://accounts.spotify.com"
URL_GET_AUTHU = "/authorize"
url_playlist = f"https://api.spotify.com/v1/users/{user_id}/playlists"
odd_songs = []
only_songs = []
only_letters_singer_list = []

date = input("please enter a date that you wanna listen to(formate: YYYY-MM-DD): ")
response = requests.get(f"{URL_BILIBOARD}{date}/)")
response = response.text
soup = BeautifulSoup(response, "html.parser")
all_songs_data = soup.find_all("h3", id="title-of-a-story")

songs_name = [i.string for i in all_songs_data]

for index in range(3, len(songs_name)):
    if index % 2 == 0:
        edit_song = songs_name[index][14:]
        edit_song = edit_song[:-5]
        odd_songs.append(edit_song)

for i in range(len(odd_songs)):
    if len(only_songs) < 100:
        if i % 2 == 1:
            only_songs.append(odd_songs[i])


all_singers= soup.find_all("span", class_="c-label")
string_list = [i.string for i in all_singers]

for index in range(len(string_list)):
        edit_song = string_list[index][4:]
        edit_song = edit_song[:-1]
        if any(char.isalpha() for char in edit_song):
            if edit_song != "NEW":
                only_letters_singer_list.append(edit_song)

get_token_headers = {
    "Authorization": f"Basic YjM1ZWE4YmEzZWExNGJhN2I3N2VmYmNmYTRkN2NmMGY6MTJmNTUxOThlN2RlNGQ0OWI3YzUzNWQyZGQwODQ0MmI=",
    "Content-Type": "application/x-www-form-urlencoded"
}

body = {
    "grant_type": "client_credentials"
}
spotify_response = requests.post(url=f"{URL_ENDPOINT}{url_get_token}", headers=get_token_headers, data=body)
if spotify_response.status_code == 200:
    # Parse the JSON response to get access token
    response_data = spotify_response.json()
    access_token = response_data["access_token"]
    print(f"there is acess token. {response_data}")
else:
    print("Error getting access token:", spotify_response.status_code, spotify_response.text)
    exit()


api_headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

data = {
    "name": "bla bla",#TODO - PUT DATE
    "description": "boom shay and naama",
    "public": False
}

# response_user_id = requests.get(url="https://api.spotify.com/v1/me", headers=api_headers)
# print(response_user_id.status_code)
# print(response_user_id.text)

response = requests.post(url_playlist, headers=api_headers, json=data)
print(response.status_code)
print(response.text)





sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="Naama Avitsur"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in only_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
