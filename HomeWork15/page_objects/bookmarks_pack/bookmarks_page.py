from HomeWork15.page_objects._base_page import BasePage
from HomeWork15.page_objects.bookmarks_pack.bookmarks_locators import BookmarksLocators
from selenium.webdriver.common.by import By
import random


class BookmarksPage:
    def __init__(self, driver):
        self._page = BasePage(driver)
        self._locators = BookmarksLocators

    def open_bookmarks(self):
        self._page.click(self._locators.loc_bookmarks)

    def create_new_folder(self, folder_name):
        self._page.click(self._locators.loc_add_new_directory)
        self._page.click(self._locators.loc_new_folder_name)
        self._page.send_keys(self._locators.loc_new_folder_name, folder_name)
        self._page.click(self._locators.loc_create_btn)

    def is_new_folder_added(self, folder_name):
        loc_folder = (By.XPATH, f'//span[@class="name"][contains(text(),"{folder_name}")]')
        return self._page.is_displayed(loc_folder)

    def delete_folder(self, folder_name):
        loc_folder_settings = (
            By.XPATH, f'//span[@class="name"][contains(text(),"{folder_name}")]/ancestor::a/following-sibling::*')
        self._page.click(loc_folder_settings)
        self._page.click(self._locators.loc_del_btn)
        self._page.accept_alert()
        self._page.driver.refresh()

    def folder_count(self):
        return self._page.get_elements_count(self._locators.loc_all_folders)

    def folder_count_without_wait(self):
        return self._page.get_elements_without_wait(self._locators.loc_all_folders)

    def rename_folder(self, folder_name, new_folder_name):
        loc_folder_settings = (
            By.XPATH, f'//span[@class="name"][contains(text(),"{folder_name}")]/ancestor::a/following-sibling::*')
        self._page.click(loc_folder_settings)
        self._page.click(self._locators.loc_rename_btn)
        self._page.hold_backspace(self._locators.loc_change_name_field)
        self._page.send_keys(self._locators.loc_change_name_field, new_folder_name)
        self._page.click(self._locators.loc_submit_change)
        self._page.click(self._locators.loc_close_button)
        self._page.driver.refresh()

    def is_new_name_appear(self, folder_name):
        loc_folder = (By.XPATH, f'//span[@class="name"][contains(text(),"{folder_name}")]')
        return self._page.is_displayed(loc_folder)

    def add_film_to_folder(self, folder_name):
        loc_folder_checkbox = (By.XPATH, f'//label[contains(text(),"{folder_name}")]')
        self._page.scroll_to_element(self._locators.loc_watch_more)
        self._page.click(self._locators.loc_add_to_bookmarks)
        self._page.click(loc_folder_checkbox)
        self._page.click(self._locators.loc_bookmarks)
        self._page.driver.refresh()

    def change_folder(self, from_folder_name, to_folder_name):
        loc_select_folder = (By.XPATH, f'//option[contains(text(),"{to_folder_name}")]')
        from_loc_folder = (By.XPATH, f'//span[@class="name"][contains(text(),"{from_folder_name}")]')
        self._page.click(from_loc_folder)
        self._page.click(self._locators.loc_film_in_checkbox)
        self._page.click(self._locators.loc_move_item)
        self._page.click(loc_select_folder)
        self._page.click(self._locators.loc_submit_change)
        self._page.accept_alert()

    def check_films_count_in_folder(self, folder_name):
        loc_folder = (By.XPATH, f'//span[@class="name"][contains(text(),"{folder_name}")]')
        self._page.click(loc_folder)
        return self._page.get_elements_without_wait(self._locators.loc_film_in_bookmarks)
