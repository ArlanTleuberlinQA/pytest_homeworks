from selenium.webdriver.common.by import By


class MainPageLocators:
    loc_items_content = (By.XPATH, '//*[@class="b-content__inline_items"]//*[@class="b-content__inline_item"]')
    loc_theme_tumbler = (By.XPATH, '//*[@class="tumbler"]')
    loc_dark_theme = (
        By.XPATH, '//*[@class="has-brand active-brand pp fixed-header no-touch b-theme__template__night"]')
    loc_white_theme = (By.XPATH, '//*[@class="has-brand active-brand pp fixed-header no-touch"]')
    loc_search_field = (By.ID, 'search-field')
    loc_cinema_mark = (By.XPATH, '//*[@class="cat films"]')
    loc_top_serials = (By.XPATH, '//*[@class="b-topnav__item i2"]//*[@href="/series/"]')
    loc_netflix = (By.XPATH, '//*[@title="Сериалы Netflix"]')
    loc_netflix_text = (By.XPATH, '//*[@class="b-content__htitle"]//*[contains(text(), "NETFLIX")]')
    loc_top_films = (By.XPATH, '//*[@class="b-topnav__item i1"]//*[@href="/films/"]')
    loc_search_category = (By.ID, 'find-best-block-1')
    loc_search_year = (By.ID, 'find-best-block-1-2')
    loc_any_cinema = (By.XPATH, '//*[@class="b-content__inline_item-link"]')
    loc_westerns = (By.XPATH, '//*[@href="/films/western/"]')
    loc_western_on_cinema_page = (By.XPATH, '//*[@id="main"]//*[@href="https://rezka.ag/films/western/"]')
    loc_settings = (By.XPATH, '//*[@href="https://rezka.ag/settings/"]')
    loc_random_film = (By.XPATH, '//div[@class="b-content__inline_items"]//div[@class="b-content__inline_item-link"]')
