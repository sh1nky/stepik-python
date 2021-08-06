from Main import Main
from selenium.webdriver.support.ui import Select
import time

browser = Main().getChrome()

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)

    sum = str(num1+num2)

    select = Select(browser.find_element_by_id('dropdown')).select_by_value(sum)

    browser.find_element_by_xpath('//button[text()="Submit"]').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


