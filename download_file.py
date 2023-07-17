from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.CSS_SELECTOR, "input:nth-child(2)")
first_name.send_keys("Alex")

last_name = browser.find_element(By.CSS_SELECTOR,"input:nth-child(4)")
last_name.send_keys("Johnson")

email_address = browser.find_element(By.CSS_SELECTOR, "input:nth-child(6)")
email_address.send_keys("tweertwerk12345@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "/Users/kirilloborok/Documents/test/file.txt"
file_path = os.path.join(current_dir, file_name)
file_name = browser.find_element(By.CSS_SELECTOR, "[type='file']")
file_name.send_keys(file_path)

submit_button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
submit_button.click()
time.sleep(5)