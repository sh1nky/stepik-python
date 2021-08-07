from Main import Main
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = Main().getChrome()

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    browser.find_element_by_class_name('trollface').click()

    browser.switch_to_window(browser.window_handles[1])

    x = int(browser.find_element_by_id('input_value').text)

    result = calc(x)

    browser.find_element_by_id('answer').send_keys(result)

    submit = browser.find_element_by_xpath('//button[text()="Submit"]').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


