from HomeWork15.page_objects.main_page_pack.main_page_locators import MainPageLocators
from HomeWork15.page_objects._base_page import BasePage


class MainPage:
    def __init__(self, driver):
        self._page = BasePage(driver)
        self._main_locators = MainPageLocators

    def items_get_count(self):
        return self._page.get_elements_count(self._main_locators.loc_items_content)

    def click_on_tumbler(self):
        return self._page.click(self._main_locators.loc_theme_tumbler)

    def is_dark_theme_displayed(self):
        return self._page.is_displayed(self._main_locators.loc_dark_theme)

    def is_white_theme_displayed(self):
        return self._page.is_displayed(self._main_locators.loc_white_theme)

    def search_cinema(self, cinema):
        self._page.click(self._main_locators.loc_search_field)
        self._page.send_keys(self._main_locators.loc_search_field, value=cinema)
        return self._page.tap_enter(self._main_locators.loc_search_field)

    def is_cinema_displayed(self):
        return self._page.is_displayed(self._main_locators.loc_cinema_mark)

    def go_to_netflix_serials(self):
        self._page.move_cursor(self._main_locators.loc_top_serials)
        return self._page.click(self._main_locators.loc_netflix)

    def is_netflix_displayed(self):
        return self._page.is_displayed(self._main_locators.loc_netflix_text)

    def search_best_westerns(self):
        self._page.move_cursor(self._main_locators.loc_top_films)
        self._page.click(self._main_locators.loc_westerns)
        return self._page.click(self._main_locators.loc_any_cinema)

    def is_western(self):
        return self._page.is_displayed(self._main_locators.loc_western_on_cinema_page)

    def click_on_random_film(self):
        self._page.click(self._main_locators.loc_any_cinema)
