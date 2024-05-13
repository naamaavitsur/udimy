# import selenium
from selenium import webdriver
import requests
# import search by:
from selenium.webdriver.common.by import By
# import keys (enter, shift..)
from selenium.webdriver.common.keys import Keys


# chrome_headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
#                   "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8,he;q=0.7"}
#
# response = requests.get("https://www.amazon.com", headers=chrome_headers)
#
#
# # keep chrome automatic open
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
#
#
# driver = webdriver.Chrome(options=chrome_option)
# driver.get(url="https://www.python.org/")
# title = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')
# # print(title.get_attribute("aria-label"))
# # print(title.size)
# time = title.get_attribute("datetime")
#
# list_of_date_xpath = ['//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]','//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]','//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]','//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]','//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]' ]
# dict_of_dicts = {}
# number = 0
# for link in list_of_date_xpath:
#     date = driver.find_elements(by=By.XPATH, value=link)
#     for i in date:
#         day = i.find_element(by=By.TAG_NAME, value="time")
#         day = day.get_attribute("datetime")[:10]
#         name = i.find_element(by=By.TAG_NAME, value="a")
#         name = name.text
#         name_date_dict = {}
#         inside_dict = {}
#         name_date_dict["name"] = name
#         name_date_dict["date"] = day
#         dict_of_dicts[number] = name_date_dict
#         number += 1
# print(dict_of_dicts)
#
# return_dict = {}
# event_time = driver.find_elements(by=By.CSS_SELECTOR, value=".last time")
# event_name = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
# for n in range(len(event_name)):
#     return_dict[n] = {
#         "name": event_name[n].text,
#         "time": event_time[n].text
#     }
# print(return_dict)
#
# # to close only one tab
# # driver.close()
# # close all chrome
# driver.quit()

# wikipedia_driver = webdriver.Chrome(options=chrome_option)
# wikipedia_driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# number_of_articls = wikipedia_driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(number_of_articls.text)
# number_of_articls.click()
# or:
# number_of_articls = wikipedia_driver.find_element(by=By.LINK_TEXT, value="English")
# number_of_articls.click()

# search_button = wikipedia_driver.find_element(by=By.CSS_SELECTOR, value=".mw-ui-icon-search")
# search_button.click()
# class="cdx-search-input cdx-search-input--has-end-button cdx-typeahead-search__input"
# search_bar = wikipedia_driver.find_element(by=By.CSS_SELECTOR, value=".cdx-text-input__input")
# search_bar.send_keys("ישראל")
# search_bar.send_keys(Keys.ENTER)


# wikipedia_driver.quit()

challenge = webdriver.Chrome(options=chrome_option)
challenge.get("https://secure-retreat-92358.herokuapp.com/")
first_name = challenge.find_element(by=By.NAME, value="fName")
first_name.send_keys("Naama")
second_name = challenge.find_element(by=By.NAME, value="lName")
second_name.send_keys("Avitsur")
email = challenge.find_element(by=By.NAME, value="email")
email.send_keys("naamaavit@gmail.com")
send_button = challenge.find_element(by=By.CSS_SELECTOR, value=".btn")
send_button.click()





