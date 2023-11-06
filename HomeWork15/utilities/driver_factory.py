from selenium.webdriver import Chrome, ChromeOptions

_CHROME_ID = 1


class DriverFactory:
    def __init__(self, browser_id: int):
        self.__browser_id = browser_id

    def get_driver(self):
        return self.__get_chrome_driver()

    @staticmethod
    def __get_chrome_driver():
        _options = ChromeOptions()
        driver = Chrome(options=_options)
        return driver
