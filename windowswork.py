from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button")
button.click()

browser.switch_to.window(window_name=browser.window_handles[1])

x = int(browser.find_element(By.ID, "input_value").text)
result = math.log(abs(12*math.sin(x)))

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(result)

submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()

alert = browser.switch_to.alert
alert.accept()

time.sleep(5)
browser.quit()
