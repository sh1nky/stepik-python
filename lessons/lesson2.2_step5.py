from Main import Main
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = Main().getChrome()

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element_by_id('input_value').text)

    result = calc(x)

    browser.find_element_by_id('answer').send_keys(result)

    checkbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    submit = browser.find_element_by_xpath('//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


