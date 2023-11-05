from HomeWork15.page_objects._base_page import BasePage
from HomeWork15.page_objects.login_page_pack.login_locators import LoginLocators
from HomeWork15.page_objects.main_page_pack.main_page import MainPage
from HomeWork15.page_objects.settings_page_pack.settings_page import SettingsPage


class LoginPage:
    def __init__(self, driver):
        self._page = BasePage(driver)
        self._login_locators = LoginLocators

    def open_login_popup(self):
        self._page.click(self._login_locators.loc_enter_btn)
        return LoginPage

    def open_reg_login_popup(self):
        self._page.click(self._login_locators.loc_registration)
        self._page.click(self._login_locators.loc_reg_login)
        return LoginPage

    def set_login(self, login: str):
        self._page.send_keys(self._login_locators.loc_username_input, value=login)
        return self

    def set_password(self, password: str):
        self._page.send_keys(self._login_locators.loc_password_input, value=password)
        return self

    def click_login_btn(self):
        self._page.click(self._login_locators.loc_login_btn)
        return LoginPage(self._page.driver)

    def bad_click_login_btn(self):
        self._page.click(self._login_locators.loc_login_btn)
        return LoginPage(self._page.driver)

    def click_logout_btn(self):
        self._page.click(self._login_locators.loc_profile)
        self._page.click(self._login_locators.loc_logout_btn)
        return LoginPage(self._page.driver)

    def click_on_forgot(self):
        self.open_login_popup()
        self._page.click(self._login_locators.loc_forgot_btn)
        return LoginPage(self._page.driver)

    def is_fail_text_displayed(self):
        return self._page.is_displayed(self._login_locators.loc_fail_text)

    def is_restore_btn_displayed(self):
        return self._page.is_displayed(self._login_locators.loc_restore_btn)

    # STEPS
    def do_login(self, login: str, password: str):
        self.open_login_popup()
        self.set_login(login)
        self.set_password(password)
        return self.click_login_btn()

    def do_reg_login(self, login: str, password: str):
        self.open_reg_login_popup()
        self.set_login(login)
        self.set_password(password)
        return self.click_login_btn()

    def do_bad_login(self, login: str, password: str):
        self.open_login_popup()
        self.set_login(login)
        self.set_password(password)
        return self.bad_click_login_btn()

    def is_profile_displayed(self):
        return self._page.is_displayed(self._login_locators.loc_profile)

    def is_enter_displayed(self):
        return self._page.is_displayed(self._login_locators.loc_enter_btn)
