import random

from selenium.common import NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.action = ActionChains(driver)

    def wait_element_is_visible(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element_is_clickable(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_element_is_presence(self, locator: tuple, timeout=10) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def send_keys(self, locator: tuple, value):
        el = self.wait_element_is_visible(locator)
        el.send_keys(value)

    def click(self, locator: tuple):
        el = self.wait_element_is_clickable(locator)
        el.click()

    def get_text(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.text

    def is_displayed(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.is_displayed()

    def get_elements_count(self, locator: tuple):
        self.wait_element_is_presence(locator)
        els = self.driver.find_elements(*locator)
        return len(els)

    def get_elements_without_wait(self, locator: tuple):
        els = self.driver.find_elements(*locator)
        return len(els)

    def tap_enter(self, locator):
        self.wait_element_is_visible(locator)
        return self.send_keys(locator, Keys.RETURN)

    def move_cursor(self, locator):
        el = self.wait_element_is_visible(locator)
        ActionChains(self.driver).move_to_element(el).perform()

    def hold_backspace(self, locator):
        self.wait_element_is_visible(locator)
        return self.send_keys(locator, Keys.BACKSPACE * 30)

    def double_click(self, locator: tuple):
        self.wait_element_is_clickable(locator)
        self.action.double_click()

    def scroll_to_element(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        ActionChains(self.driver).scroll_to_element(el).perform()

    def wait_element_is_invisible(self, locator: tuple, timeout=120) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element(locator))

    def is_presence(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        return el.is_displayed()

    def is_invisible(self, locator):
        self.wait_element_is_visible(locator)
        self.wait_element_is_invisible(locator)

    def switch_to_frame(self, locator):
        el = self.wait_element_is_visible(locator)
        self.driver.switch_to.frame(el)

    def click_on_random_element(self, locator):
        self.wait_element_is_presence(locator)
        els = self.driver.find_elements(*locator)
        random_film = random.choice(els)
        self.scroll_to_element(random_film)
        self.click(random_film)

    def accept_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass




