from selenium.webdriver.common.by import By


class LoginLocators:
    loc_profile = (By.XPATH, '//*[@id="top-head"]/div/div[2]/span')
    loc_enter_btn = (By.XPATH, '//*[@id="top-head"]/div/div[2]/a[1]')
    loc_logout_btn = (By.XPATH, '//*[@id="top-head"]/div/div[2]/span/ul/li[2]/a')
    loc_registration = (By.XPATH, '//*[@id="top-head"]/div/div[2]/a[2]')
    loc_username_input = (By.XPATH, '//*[@id="login_name"]')
    loc_password_input = (By.XPATH, '//*[@id="login_password"]')
    loc_login_btn = (By.XPATH, '//*[@id="login-popup"]/div[2]/div/div[1]/form/div[3]/div/button')
    loc_reg_login = (By.XPATH, '//*[@id="register-popup"]/div[2]/div/div[2]/a')
    loc_fail_text = (By.XPATH, '//*[@id="login-popup-errors"]/li')
    loc_restore_btn = (By.XPATH, '//*[@id="main"]/div[4]/form/div[2]/table/tbody/tr[2]/td/button')
    loc_forgot_btn = (By.XPATH, '//*[@id="login-popup"]/div[2]/div/div[1]/form/div[3]/a')
    loc_settings = (By.XPATH, '//*[@href="https://rezka.ag/settings/"]')


