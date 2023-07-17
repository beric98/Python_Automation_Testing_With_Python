from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin

# Функция для решения математической задачи
def calc(x):
    return str(log(abs(12*sin(int(x)))))

# Инициализация драйвера
browser = webdriver.Chrome()  # Используйте свой драйвер браузера

try:
    # Открытие страницы
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидание, пока цена дома не станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажатие на кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # Решение математической задачи
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)

    # Ввод решения в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(answer)

    # Отправка формы
    browser.find_element(By.ID, "solve").click()

    # Получение результата
    result = browser.switch_to.alert.text.split()[-1]

finally:
    # Закрытие браузера
    browser.quit()

# Вывод результата
print("Результат:", result)
