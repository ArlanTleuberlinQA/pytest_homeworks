from selenium.webdriver.common.by import By


class BookmarksLocators:
    folder_name = ""
    loc_bookmarks = (By.XPATH, '//a[@href="https://rezka.ag/favorites/"]')
    loc_add_new_directory = (By.XPATH, '//a[@class="b-userset__fav_link"]')
    loc_all_folders = (By.XPATH, '//*[@class="b-favorites_content__cats_list_link"]')
    loc_del_btn = (By.ID, 'ps-favorites-remove')
    loc_rename_btn = (By.XPATH, '//span[@class="change-name-link"]')
    loc_add_to_bookmarks = (By.XPATH, '//button[@class="btn btn-helper add-favorite"]')
    loc_film_in_bookmarks = (By.XPATH, '//div[@class="b-content__inline_item-cover"]//i[contains(text(),"Фильм")]')
    loc_film_in_checkbox = (By.XPATH, '//*[@class="b-content__inline_items b-favorites_content__holder"]//div//label')
    loc_move_item = (By.XPATH, '//button[@class="btn btn-action btn-mini move-items"]')
    loc_open_select_folder = (By.ID, 'ps-favorites-select-cat')
    loc_submit_change = (By.XPATH, '//button[@type="submit"]')
    loc_new_folder_name = (By.ID, 'addcat-fav-name')
    loc_create_btn = (By.ID, 'addcat-fav-addbt')
    loc_change_name_field = (By.XPATH, '//input[@class="change-name-field"]')
    loc_close_button = (By.ID, 'ps-close')
    loc_watch_more = (By.XPATH, '//div[contains(text(),"отзыв")]')
