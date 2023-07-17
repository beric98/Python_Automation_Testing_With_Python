import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "input_value").text)
    result = math.log(abs(12*math.sin(x)))

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button.click()


finally:
    time.sleep(30)
    browser.quit()


