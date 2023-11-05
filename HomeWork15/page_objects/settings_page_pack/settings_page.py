from HomeWork15.page_objects.main_page_pack.main_page_locators import MainPageLocators
from HomeWork15.page_objects._base_page import BasePage
from HomeWork15.page_objects.settings_page_pack.settings_locators import SettingsPageLocators


class SettingsPage:
    def __init__(self, driver):
        self._page = BasePage(driver)
        self._sett_locators = SettingsPageLocators

    def open_settings(self):
        self._page.click(self._sett_locators.loc_profile)
        self._page.click(self._sett_locators.loc_settings)
        return SettingsPage

    def change_gender_to_male(self):
        self._page.click(self._sett_locators.loc_choose_gender)
        self._page.click(self._sett_locators.loc_gender_male)
        return self._page.click(self._sett_locators.loc_save_button)

    def change_gender_to_female(self):
        self._page.click(self._sett_locators.loc_choose_gender)
        self._page.click(self._sett_locators.loc_gender_female)
        return self._page.click(self._sett_locators.loc_save_button)

    def is_male_gender_displayed(self):
        return self._page.is_displayed(self._sett_locators.loc_selected_male_gender)

    def is_female_gender_displayed(self):
        return self._page.is_displayed(self._sett_locators.loc_selected_female_gender)

    def change_email(self, mail):
        self._page.hold_backspace(self._sett_locators.loc_current_email)
        self._page.send_keys(self._sett_locators.loc_current_email, mail)
        self._page.click(self._sett_locators.loc_save_button)

    def is_email_changed(self):
        return self._page.is_displayed(self._sett_locators.loc_changed_email)

    def change_email_to_default(self, default_mail):
        self.open_settings()
        self._page.hold_backspace(self._sett_locators.loc_changed_email)
        self._page.send_keys(self._sett_locators.loc_changed_email, default_mail)
        self._page.click(self._sett_locators.loc_save_button)

    def change_password(self, password, new_password):
        self._page.click(self._sett_locators.loc_security_tab)
        self._page.send_keys(self._sett_locators.loc_current_pass, password)
        self._page.send_keys(self._sett_locators.loc_new_pass, new_password)
        self._page.send_keys(self._sett_locators.loc_repeat_pass, new_password)
        self._page.click(self._sett_locators.loc_save_button)

    def backup_password(self, password, new_password):
        self.open_settings()
        self._page.click(self._sett_locators.loc_security_tab)
        self._page.send_keys(self._sett_locators.loc_current_pass, new_password)
        self._page.send_keys(self._sett_locators.loc_new_pass, password)
        self._page.send_keys(self._sett_locators.loc_repeat_pass, password)
        self._page.click(self._sett_locators.loc_save_button)

    def make_payment(self, payer_name):
        self._page.click(self._sett_locators.loc_promo_tab)
        self._page.click(self._sett_locators.loc_continue_btn)
        self._page.click(self._sett_locators.loc_yes_btn)
        self._page.click(self._sett_locators.loc_1mont_sub)
        self._page.click(self._sett_locators.loc_yes_payment_btn)
        self._page.click(self._sett_locators.loc_go_to_payment_btn)
        self._page.click(self._sett_locators.loc_monobank_api)
        self._page.click(self._sett_locators.loc_confirm_bank)
        self._page.click(self._sett_locators.loc_accept_terms)
        self._page.click(self._sett_locators.loc_made_payment)
        self._page.click(self._sett_locators.loc_yes_final_btn)
        self._page.click(self._sett_locators.loc_no_receipt_btn)
        self._page.send_keys(self._sett_locators.loc_name_payer, payer_name)
        self._page.click(self._sett_locators.loc_confirm_payment)

    def is_pay_success(self):
        return self._page.is_displayed(self._sett_locators.loc_loader_after_payment)

    def open_payment_history(self):
        self._page.click(self._sett_locators.loc_promo_tab)
        self._page.click(self._sett_locators.loc_payment_history)
        self._page.click(self._sett_locators.loc_last_tansaction)

    def is_sum_displayed(self):
        return self._page.is_displayed(self._sett_locators.last_transaction_sum_locator)
