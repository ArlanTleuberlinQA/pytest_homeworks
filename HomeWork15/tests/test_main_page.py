import pytest


@pytest.mark.regression_cases
def test_check_films_count(open_main_page):
    main_page = open_main_page
    exc_count = 36
    assert exc_count == main_page.items_get_count(), f'Films count must be {exc_count}'


@pytest.mark.smoke_cases
def test_theme_changing(open_main_page):
    main_page = open_main_page
    main_page.click_on_tumbler()
    assert main_page.is_dark_theme_displayed(), "Theme doesn't changing"
    main_page.click_on_tumbler()
    assert main_page.is_white_theme_displayed(), "Theme doesn't changing"


@pytest.mark.smoke_cases
def test_search_cinema(open_main_page, get_film):
    main_page = open_main_page
    main_page.search_cinema(get_film)
    assert main_page.is_cinema_displayed(), "Cinema doesn't displayed or element not a cinema"


@pytest.mark.regression_cases
def test_netflix_series(open_main_page):
    main_page = open_main_page
    main_page.go_to_netflix_serials()
    assert main_page.is_netflix_displayed(), "Text doesn't displayed or this is not Netflix serials"


@pytest.mark.regression_cases
def test_best_westerns_search(open_main_page):
    m_page = open_main_page
    m_page.search_best_westerns()
    assert m_page.is_western(), "Not a western"
