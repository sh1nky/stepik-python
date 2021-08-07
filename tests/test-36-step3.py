import pytest
import time
import math

@pytest.fixture(scope="function")
def answer():
    answer = math.log(int(time.time()))
    return str(answer)


@pytest.mark.parametrize('url', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
])
def test_text_correct_with_parameters(browser, answer, url):
    link = url
    browser.get(link)
    browser.find_element_by_class_name("ember-text-area").send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()
    result_text = browser.find_element_by_class_name("smart-hints__hint").text

    assert "Correct!" == result_text, "message=" + result_text
