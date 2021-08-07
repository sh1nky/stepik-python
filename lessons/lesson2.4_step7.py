from Main import Main
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = Main().getChrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element_by_id('book').click()

    x = int(browser.find_element_by_id('input_value').text)

    result = calc(x)
    browser.find_element_by_id('answer').send_keys(result)
    submit = browser.find_element_by_xpath('//button[text()="Submit"]').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
