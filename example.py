import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

chest = browser.find_element(By.ID, "treasure")
x_value = chest.get_attribute("valuex")

# высчитываем результат для первого задания
first_test_result = calc(x_value)

# вводим ответ к первому тесту
first_test_input = browser.find_element(By.ID, "answer")
first_test_input.send_keys(first_test_result)

# выбираем checkbox
robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
robot_checkbox.click()

# выбираем radiobutton
robot_radiobutton =browser.find_element(By.ID, "robotsRule")
robot_radiobutton.click()

# нажимаем кнопку отправить
send_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
send_button.click()

time.sleep(20)