import allure
import pytest


@pytest.mark.ui
@allure.story("Test changing gender")
@allure.title("Verify gender change")
@allure.description("This test verifies the ability to change gender in the settings.")
@allure.tag("Settings Page", "Gender")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke_cases
def test_change_gender(open_settings_page):
    set_page = open_settings_page
    set_page.change_gender_to_male()
    assert set_page.is_male_gender_displayed(), "Gender doesn't changed"
    set_page.change_gender_to_female()
    assert set_page.is_female_gender_displayed(), "Gender doesn't changed"


@pytest.mark.ui
@allure.story("Test changing email")
@allure.title("Verify email change")
@allure.description("This test verifies the ability to change email in the settings.")
@allure.tag("Settings Page", "Email")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
def test_change_email(open_settings_page, get_email, get_test_email):
    set_page = open_settings_page
    set_page.change_email(get_test_email)
    assert set_page.is_email_changed(), "Email doesn't changed"
    set_page.change_email_to_default(get_email)


@pytest.mark.ui
@allure.story("Test changing password")
@allure.title("Verify password change")
@allure.description("This test verifies the ability to change password in the settings.")
@allure.tag("Settings Page", "Password")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
def test_change_password(open_settings_page, open_login_page, get_wrong_user, get_password, get_test_password):
    s_page = open_settings_page
    s_page.change_password(get_password, get_test_password)
    l_page = open_login_page
    l_page.click_logout_btn()
    assert l_page.do_bad_login(*get_wrong_user)
    s_page.backup_password(get_password, get_test_password)


@pytest.mark.ui
@pytest.mark.smoke_cases
def test_payment(open_settings_page, get_name_payer):
    s_page = open_settings_page
    s_page.make_payment(get_name_payer)
    assert s_page.is_pay_success()


@pytest.mark.ui
@allure.story("Test payment history")
@allure.title("Verify last payment in history")
@allure.description("This test verifies the last payment in the payment history in the settings.")
@allure.tag("Settings Page", "Payment History")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
def test_the_last_payment_in_history(open_settings_page):
    s_page = open_settings_page
    s_page.open_payment_history()
    assert s_page.is_sum_displayed()
