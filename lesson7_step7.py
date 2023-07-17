from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.NAME, ("firstname"))

    for element in elements:
        element.send_keys("1")

    elements = browser.find_elements(By.NAME, ("lastname"))

    for element in elements:
        element.send_keys("2")

    elements = browser.find_elements(By.NAME, ("e-mail"))

    for element in elements:
        element.send_keys("3")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(11)"))

    for element in elements:
        element.send_keys("4")

    for element in elements:
        element.send_keys("5")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(14)"))

    for element in elements:
        element.send_keys("6")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(17)"))

    for element in elements:
        element.send_keys("7")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(20)"))

    for element in elements:
        element.send_keys("8")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(23)"))

    for element in elements:
        element.send_keys("9")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(26)"))

    for element in elements:
        element.send_keys("10")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(29)"))

    for element in elements:
        element.send_keys("11")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(32)"))

    for element in elements:
        element.send_keys("12")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(35)"))

    for element in elements:
        element.send_keys("13")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(38)"))

    for element in elements:
        element.send_keys("14")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(41)"))

    for element in elements:
        element.send_keys("15")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(44)"))

    for element in elements:
        element.send_keys("16")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(50)"))

    for element in elements:
        element.send_keys("17")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(53)"))

    for element in elements:
        element.send_keys("18")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(56)"))

    for element in elements:
        element.send_keys("20")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(59)"))

    for element in elements:
        element.send_keys("21")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(62)"))

    for element in elements:
        element.send_keys("22")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(65)"))

    for element in elements:
        element.send_keys("23")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(68)"))

    for element in elements:
        element.send_keys("24")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(71)"))

    for element in elements:
        element.send_keys("25")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(74)"))

    for element in elements:
        element.send_keys("26")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(77)"))

    for element in elements:
        element.send_keys("27")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(80)"))

    for element in elements:
        element.send_keys("28")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(83)"))

    for element in elements:
        element.send_keys("29")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(86)"))

    for element in elements:
        element.send_keys("30")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(89)"))

    for element in elements:
        element.send_keys("31")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(92)"))

    for element in elements:
        element.send_keys("32")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(95)"))

    for element in elements:
        element.send_keys("33")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(98)"))

    for element in elements:
        element.send_keys("34")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(101)"))

    for element in elements:
        element.send_keys("35")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(104)"))

    for element in elements:
        element.send_keys("36")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(107)"))

    for element in elements:
        element.send_keys("37")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(110)"))

    for element in elements:
        element.send_keys("38")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(113)"))

    for element in elements:
        element.send_keys("39")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(116)"))

    for element in elements:
        element.send_keys("40")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(119)"))

    for element in elements:
        element.send_keys("41")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(122)"))

    for element in elements:
        element.send_keys("42")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(125)"))

    for element in elements:
        element.send_keys("43")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(128)"))

    for element in elements:
        element.send_keys("44")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(131)"))

    for element in elements:
        element.send_keys("45")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(134)"))

    for element in elements:
        element.send_keys("46")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(137)"))

    for element in elements:
        element.send_keys("47")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(140)"))

    for element in elements:
        element.send_keys("48")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(143)"))

    for element in elements:
        element.send_keys("49")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(146)"))

    for element in elements:
        element.send_keys("50")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(149)"))

    for element in elements:
        element.send_keys("51")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(152)"))

    for element in elements:
        element.send_keys("52")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(155)"))

    for element in elements:
        element.send_keys("53")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(158)"))

    for element in elements:
        element.send_keys("54")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(161)"))

    for element in elements:
        element.send_keys("55")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(164)"))

    for element in elements:
        element.send_keys("56")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(167)"))

    for element in elements:
        element.send_keys("57")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(170)"))

    for element in elements:
        element.send_keys("58")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(173)"))

    for element in elements:
        element.send_keys("59")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(176)"))

    for element in elements:
        element.send_keys("60")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(179)"))

    for element in elements:
        element.send_keys("61")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(182)"))

    for element in elements:
        element.send_keys("62")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(185)"))

    for element in elements:
        element.send_keys("63")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(188)"))

    for element in elements:
        element.send_keys("64")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(191)"))

    for element in elements:
        element.send_keys("65")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(194)"))

    for element in elements:
        element.send_keys("66")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(197)"))

    for element in elements:
        element.send_keys("67")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(200)"))

    for element in elements:
        element.send_keys("68")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(203)"))

    for element in elements:
        element.send_keys("69")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(206)"))

    for element in elements:
        element.send_keys("70")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(209)"))

    for element in elements:
        element.send_keys("71")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(215)"))

    for element in elements:
        element.send_keys("72")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(218)"))

    for element in elements:
        element.send_keys("73")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(221)"))

    for element in elements:
        element.send_keys("74")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(224)"))

    for element in elements:
        element.send_keys("75")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(227)"))

    for element in elements:
        element.send_keys("76")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(230)"))

    for element in elements:
        element.send_keys("77")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(233)"))

    for element in elements:
        element.send_keys("78")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(236)"))

    for element in elements:
        element.send_keys("79")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(239)"))

    for element in elements:
        element.send_keys("80")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(242)"))

    for element in elements:
        element.send_keys("81")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(245)"))

    for element in elements:
        element.send_keys("82")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(248)"))

    for element in elements:
        element.send_keys("83")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(251)"))

    for element in elements:
        element.send_keys("84")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(254)"))

    for element in elements:
        element.send_keys("85")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(257)"))

    for element in elements:
        element.send_keys("86")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(260)"))

    for element in elements:
        element.send_keys("87")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(263)"))

    for element in elements:
        element.send_keys("88")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(269)"))

    for element in elements:
        element.send_keys("89")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(272)"))

    for element in elements:
        element.send_keys("90")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(275)"))

    for element in elements:
        element.send_keys("91")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(278)"))

    for element in elements:
        element.send_keys("92")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(281)"))

    for element in elements:
        element.send_keys("93")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(284)"))

    for element in elements:
        element.send_keys("94")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(287)"))

    for element in elements:
        element.send_keys("95")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(290)"))

    for element in elements:
        element.send_keys("96")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(293)"))

    for element in elements:
        element.send_keys("97")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(296)"))

    for element in elements:
        element.send_keys("98")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(299)"))

    for element in elements:
        element.send_keys("99")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(47)"))

    for element in elements:
        element.send_keys("100")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(266)"))

    for element in elements:
        element.send_keys("101")

    elements = browser.find_elements(By.CSS_SELECTOR, ("input[type=text]:nth-child(212)"))

    for element in elements:
        element.send_keys("102")










    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла