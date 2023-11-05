from HomeWork15.page_objects._base_page import BasePage
from HomeWork15.page_objects.serial_page_pack.serial_locators import SerialPageLocators


class SerialPage:
    def __init__(self, driver):
        self._page = BasePage(driver)
        self._serial_locators = SerialPageLocators

    def change_season_to_2(self):
        self._page.scroll_to_element(self._serial_locators.loc_play_pause_button)
        self._page.click(self._serial_locators.loc_season_2)

    def is_season_changed(self):
        return self._page.is_displayed(self._serial_locators.loc_season_2_active)

    def change_dub_to_ukr(self):
        self._page.scroll_to_element(self._serial_locators.loc_play_pause_button)
        self._page.click(self._serial_locators.loc_ukr_dub)

    def is_dub_changed(self):
        return self._page.is_displayed(self._serial_locators.loc_ukr_dub_is_active)

    def play_video(self):
        self._page.scroll_to_element(self._serial_locators.loc_comments_list)
        self._page.click(self._serial_locators.loc_play_pause_button)

    def is_ads_appear(self):
        return self._page.is_presence(self._serial_locators.loc_ads_on_screen)

    def wait_till_ads_disappear(self):
        return self._page.is_invisible(self._serial_locators.loc_ads_on_screen)

    def is_timecode_appear(self):
        self._page.move_cursor(self._serial_locators.loc_player)
        return self._page.is_displayed(self._serial_locators.loc_video_playing)

    def play_trailer(self):
        self._page.click(self._serial_locators.loc_mentalist_trailer)

    def is_trailer_autoplay(self):
        self._page.switch_to_frame(self._serial_locators.loc_google_player)
        return self._page.is_displayed(self._serial_locators.loc_playing_trailer)
