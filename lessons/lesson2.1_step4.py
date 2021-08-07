from Main import Main
import time
import math

browser = Main().getFirefox()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_xpath('//button[text()="Submit"]').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


