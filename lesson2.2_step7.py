from Main import Main
from selenium.webdriver.support.ui import Select
import time
import os

browser = Main().getChrome()

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('Name')
    browser.find_element_by_name('lastname').send_keys('Last')
    browser.find_element_by_name('email').send_keys('a@b.c')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'help\\test.txt')

    browser.find_element_by_id('file').send_keys(file_path)

    browser.find_element_by_xpath('//button[text()="Submit"]').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


