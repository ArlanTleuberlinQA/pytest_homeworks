import pytest


@pytest.mark.smoke_cases
def test_create_folder(open_bookmarks_page, get_random_folder_name):
    b_page = open_bookmarks_page
    b_page.create_new_folder(get_random_folder_name)
    assert b_page.is_new_folder_added(get_random_folder_name), "Folder doesn't created"


@pytest.mark.smoke_cases
def test_delete_folder(open_bookmarks_page, get_default_folder_name):
    b_page = open_bookmarks_page
    el_before = b_page.folder_count()
    b_page.delete_folder(get_default_folder_name)
    assert b_page.folder_count_without_wait() == el_before - 1, "Folder doesn't deleted"
    b_page.create_new_folder(get_default_folder_name)


@pytest.mark.regression_cases
def test_rename_folder(open_bookmarks_page, get_default_folder_name):
    b_page = open_bookmarks_page
    new_name = "New_name"
    b_page.rename_folder(get_default_folder_name, new_name)
    assert b_page.is_new_name_appear(new_name), "Folder doesn't renamed"
    b_page.rename_folder(new_name, get_default_folder_name)


@pytest.mark.smoke_cases
def test_add_film(open_main_page, open_bookmarks_page, get_film, get_default_folder_name):
    b_page = open_bookmarks_page
    films_before = b_page.check_films_count_in_folder(get_default_folder_name)
    m_page = open_main_page
    m_page.search_cinema(get_film)
    m_page.click_on_random_film()
    b_page.add_film_to_folder(get_default_folder_name)
    assert b_page.check_films_count_in_folder(get_default_folder_name) == films_before + 1, "Cinema doesn't added"


@pytest.mark.regression_cases
def test_change_film_folder(open_bookmarks_page, get_default_folder_name):
    b_page = open_bookmarks_page
    to_folder = "Move here"
    before_from = b_page.check_films_count_in_folder(get_default_folder_name)
    before_to = b_page.check_films_count_in_folder(to_folder)
    b_page.change_folder(get_default_folder_name, to_folder)
    assert b_page.check_films_count_in_folder(get_default_folder_name) == before_from - 1
    assert b_page.check_films_count_in_folder(to_folder) == before_to + 1
