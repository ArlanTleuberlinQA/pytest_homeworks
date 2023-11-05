from selenium.webdriver.common.by import By


class SerialPageLocators:
    loc_player = (By.ID, 'cdnplayer-container')
    loc_season_2 = (By.XPATH, '//*[@data-tab_id="2"]')
    loc_season_2_active = (By.XPATH, '//*[@class="b-simple_season__item active"][contains(text(), "2")]')
    loc_play_pause_button = (By.XPATH, '//*[@id="oframecdnplayer"]/pjsdiv[6]/pjsdiv[1]/pjsdiv')
    loc_ads_on_screen = (By.XPATH, '//*[@id="oframecdnplayer"]//*[contains(text(), "Реклама")]')
    loc_ukr_dub = (By.XPATH, '//*[@data-translator_id="359"]')
    loc_mentalist_trailer = (By.XPATH, '//*[@data-id="1741"]')
    loc_playing_trailer = (
        By.XPATH, '//*[@id="movie_player"]/div[28]/div[2]/div[1]/button')
    loc_video_playing = (By.XPATH, '//noindex[contains(text(),"0:01")]')
    loc_ukr_dub_is_active = (By.XPATH, '//*[@data-translator_id="359"][contains(@class, "b-translator__item active")]')
    loc_comments_list = (By.ID, 'comments-list-button')
    loc_google_player = (By.XPATH, '//iframe[contains(@width,"640")]')
