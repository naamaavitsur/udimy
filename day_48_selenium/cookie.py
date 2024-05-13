from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
import datetime
import re


# def make_dict_of_product():
#     list_of_price = []
#     for item in list_of_product:
#         list_of_value = item.text.split(" ")
#         value = list_of_value[-1]
#         value = value.replace(",", "")
#         if value.isdigit():
#             value = int(value)
#             list_of_price.append(value)
#     for _ in range(len(list_of_product)):
#         # TODO check enum
#         element_item = list_of_click_divs[_]
#         money_amount_item = list_of_price[_]
#         dict_of_product[element_item] = money_amount_item


def try_to_click(driver):
    store = driver.find_element(by=By.CSS_SELECTOR, value="#store")
    list_of_click_divs = store.find_elements(by=By.TAG_NAME, value="div")
    for e in list_of_click_divs[::-1]:
        try:
            e.click()
        except StaleElementReferenceException:
            print(f"can't click")
        except ElementNotInteractableException:
            print("not clickable")
        except KeyError as e:
            print(e)
        except Exception as e:
            print(e)
    return



# def check_if_can_buy(dict_of_elements):  # {div_elem: price}
#     print(f"in check_if_can_buy: {dict_of_elements}")
#     current_money = get_money()
#     for product_div in dict_of_elements:
#         if dict_of_elements[product_div] < current_money:
#             print(dict_of_elements[product_div])
#             print(current_money)
#             print(datetime.datetime.now())
#             try:
#                 product_div.click()
#             except StaleElementReferenceException:
#                 print("new exception")


# def get_money():
#     current_money = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#money").text
#     current_money = current_money.replace(",", "")
#     if not current_money.isdigit():
#         print("problem with money:")
#         print(current_money)
#         print(type(current_money))
#         quit(1)
#     current_money = int(current_money)
#     return current_money
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
cookie_driver = webdriver.Chrome(options=chrome_option)
cookie_driver.get("https://orteil.dashnet.org/experiments/cookie/")
click_on_cookie = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#cookie")
divs_list = cookie_driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
id_list = [item.get_attribute("id") for item in divs_list]
five_sec = datetime.timedelta(seconds=5)
start_point = datetime.datetime.now()
five_min_from_start = start_point + datetime.timedelta(minutes=5)
after_five_sec = start_point + five_sec
while True:
    click_on_cookie.click()
    current = datetime.datetime.now()
    if current > five_min_from_start:
        cookie_per_second = cookie_driver.find_element(by=By.ID, value="cps").text
        print(f"done! your cookies per second: {cookie_per_second}")
        cookie_driver.quit() 
        exit(0)
    if current > after_five_sec:
        after_five_sec = current + five_sec
        print(f"now {current}")
        curent_money = cookie_driver.find_element(by=By.ID, value="money").text
        curent_money = int(curent_money.replace(",", ""))
        print(curent_money)
        for item in id_list[::-1]:
            product_click_element = cookie_driver.find_element(by=By.ID, value=item)
            if item != "":
                print(item)
                try:
                    product_amount = product_click_element.find_element(by=By.TAG_NAME, value="b").text
                    print(product_amount)
                    product_amount = product_amount.split(" ")[-1]
                    product_amount = product_amount.replace(",", "")
                    product_amount = int(product_amount)
                    if curent_money > product_amount:
                        product_click_element.click()
                        curent_money = cookie_driver.find_element(by=By.ID, value="money").text
                        curent_money = int(curent_money.replace(",", ""))
                        print(f"i click {item}")
                except:
                    continue



