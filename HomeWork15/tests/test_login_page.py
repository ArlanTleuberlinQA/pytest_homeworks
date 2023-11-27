import pytest
import allure


@pytest.mark.ui
@allure.story("Test login")
@allure.title("Verify successful login")
@allure.description("This test verifies successful login to the web-site.")
@allure.tag("Authentication")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke_cases
def test_login(open_login_page, get_user):
    main_page = open_login_page.do_login(*get_user)
    assert main_page.is_profile_displayed(), 'Login failed, profile not displayed'


@pytest.mark.ui
@allure.story("Test logout")
@allure.title("Verify successful logout")
@allure.description("This test verifies successful logout from the web-site.")
@allure.tag("Authentication")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke_cases
def test_logout(open_login_page, get_user):
    l_page = open_login_page
    l_page.do_login(*get_user).click_logout_btn()
    assert l_page.is_enter_displayed(), 'Logout failed, enter not displayed'


@pytest.mark.ui
@allure.story("Test login through registration")
@allure.title("Verify login through registration")
@allure.description("This test verifies login through the registration process.")
@allure.tag("Authentication")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
@pytest.mark.regression_cases
def test_login_throw_registration(open_login_page, get_user):
    main_page = open_login_page
    main_page.do_reg_login(*get_user)
    assert main_page.is_profile_displayed(), 'Login failed, profile not displayed'


@pytest.mark.ui
@allure.story("Test incorrect password")
@allure.title("Verify incorrect password login")
@allure.description("This test verifies login with an incorrect password.")
@allure.tag("Authentication")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
def test_incorrect_password(open_login_page, get_wrong_user):
    login_page = open_login_page.do_bad_login(*get_wrong_user)
    assert login_page.is_fail_text_displayed(), 'Fail text not displayed'


@pytest.mark.ui
@allure.story("Test forgot password")
@allure.title("Verify forgot password functionality")
@allure.description("This test verifies the functionality of the 'Forgot Password' feature.")
@allure.tag("Authentication")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
def test_forgot_password(open_login_page):
    forgot_page = open_login_page.click_on_forgot()
    assert forgot_page.is_restore_btn_displayed()
