import pytest


@pytest.mark.smoke_cases
def test_login(open_login_page, get_user):
    main_page = open_login_page.do_login(*get_user)
    assert main_page.is_profile_displayed(), 'Login failed, profile not displayed'


@pytest.mark.smoke_cases
def test_logout(open_login_page, get_user):
    l_page = open_login_page
    l_page.do_login(*get_user).click_logout_btn()
    assert l_page.is_enter_displayed(), 'Logout failed, enter not displayed'


@pytest.mark.regression_cases
def test_login_throw_registration(open_login_page, get_user):
    main_page = open_login_page
    main_page.do_reg_login(*get_user)
    assert main_page.is_profile_displayed(), 'Login failed, profile not displayed'


@pytest.mark.regression_cases
def test_incorrect_password(open_login_page, get_wrong_user):
    login_page = open_login_page.do_bad_login(*get_wrong_user)
    assert login_page.is_fail_text_displayed(), 'Fail text not displayed'


@pytest.mark.regression_cases
def test_forgot_password(open_login_page):
    forgot_page = open_login_page.click_on_forgot()
    assert forgot_page.is_restore_btn_displayed()
