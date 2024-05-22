from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
tinder_driver = webdriver.Chrome(options=chrome_option)
tinder_driver.get(url= "https://tinder.com/")
sleep(4)
log_in = tinder_driver.find_element(by=By.XPATH, value='//*[@id="u605472098"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]')
log_in.click()
sleep(2)
log_in_facebook = tinder_driver.find_element(by=By.XPATH, value='//*[@id="u-1122908978"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
sleep(2)
