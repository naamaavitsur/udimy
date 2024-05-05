from bs4 import BeautifulSoup
import requests

# with open("website.html", "r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
#
# all_anchore_tags = soup.findAll("a")
# for tag in all_anchore_tags:
#     print(tag.get("href"))
#
# print(soup.find(id="name"))
# print(soup.select("#name"))
# print(soup.select_one(".heading"))
# list_of_link = []
# list_of_titles = []
# list_of_score = []
#
# response = requests.get("https://news.ycombinator.com/news")
# soup = BeautifulSoup(response.text, "html.parser")
# all_a_tag = soup.findAll("span", class_="titleline")
# for tag in all_a_tag:
#     a = tag.find("a")
#     url = a.get("href")
#     title = a.string
#     list_of_link.append(url)
#     list_of_titles.append(title)
#     # print(f"url :{url}, title: {title}")
# all_score = soup.findAll("span", class_= "score")
# for score in all_score:
#     only_score = score.getText()
#     list = only_score.split(" ")
#     list_of_score.append(int(list[0]))
# max_index = list_of_score.index(max(list_of_score))
# print(f"the best article is: {list_of_titles[max_index+1]}.\nthis artucle have score of:{list_of_score[max_index]}\nurl: {list_of_link[max_index+1]}")
# print(list_of_score)
# print(list_of_titles)


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response = response.text
soup = BeautifulSoup(response, "html.parser")
all_movie = soup.findAll("h3", class_="listicleItem_listicle-item__title__BfenH")
print(all_movie)
list_of_movies = []
for i in all_movie:
    movie_name = i.string
    list_of_movies.append(movie_name)
with open("100 best movie.txt", "w") as file:
    for number in range(1, len(list_of_movies)+1):
        file.write(f"{list_of_movies[-number]}\n")




