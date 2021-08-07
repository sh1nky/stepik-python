import time
import pytest

class TestAbs:

    @pytest.mark.regress
    def test01(self, browser):
        link = "https://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(".first:required").send_keys("Ivan")
        browser.find_element_by_css_selector(".second:required").send_keys("Ivanov")
        browser.find_element_by_css_selector(".third:required").send_keys("a@b.c")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test02(self, browser):
        link = "https://suninjuly.github.io/registration2.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(".first:required").send_keys("Ivan")
        browser.find_element_by_css_selector(".second:required").send_keys("Ivanov")
        browser.find_element_by_css_selector(".third:required").send_keys("a@b.c")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
