from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

CHROME_DRIVER_PATH = 'Selenium/chromedriver.exe'
FIREFOX_DRIVER_PATH = 'Selenium/firefox.exe'


class Main:

    def __init__(self):
        self.driver = webdriver

    def __del__(self):
        del self.driver

    def getChrome(self):
        return self.driver.Chrome(executable_path=ChromeDriverManager().install())

    def getFirefox(self):
        return self.driver.Firefox(executable_path=GeckoDriverManager().install())
