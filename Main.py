from selenium import webdriver

CHROME_DRIVER_PATH = 'selenium/chromedriver.exe'
FIREFOX_DRIVER_PATH = 'selenium/firefox.exe'


class Main:

    def __init__(self):
        self.driver = webdriver

    def __del__(self):
        del self.driver

    def getChrome(self):
        return self.driver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def getFirefox(self):
        return self.driver.Chrome(executable_path=FIREFOX_DRIVER_PATH)
