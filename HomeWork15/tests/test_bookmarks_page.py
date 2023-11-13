import pytest
import allure


@allure.story("Test creating a folder")
@allure.title("Verify creating a folder")
@allure.description("This test verifies the ability to create a new folder in the bookmarks.")
@allure.tag("Bookmarks", "Folders")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke_cases
def test_create_folder(open_bookmarks_page, get_random_folder_name):
    b_page = open_bookmarks_page
    b_page.create_new_folder(get_random_folder_name)
    assert b_page.is_new_folder_added(get_random_folder_name), "Folder doesn't created"


@allure.story("Test deleting a folder")
@allure.title("Verify deleting a folder")
@allure.description("This test verifies the ability to delete a folder in the bookmarks.")
@allure.tag("Bookmarks", "Folders")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke_cases
def test_delete_folder(open_bookmarks_page, get_default_folder_name):
    b_page = open_bookmarks_page
    el_before = b_page.folder_count()
    b_page.delete_folder(get_default_folder_name)
    assert b_page.folder_count_without_wait() == el_before - 1, "Folder doesn't deleted"
    b_page.create_new_folder(get_default_folder_name)


@allure.story("Test renaming a folder")
@allure.title("Verify renaming a folder")
@allure.description("This test verifies the ability to rename a folder in the bookmarks.")
@allure.tag("Bookmarks", "Folders")
@pytest.mark.regression_cases
def test_rename_folder(open_bookmarks_page, get_default_folder_name):
    b_page = open_bookmarks_page
    new_name = "New_name"
    b_page.rename_folder(get_default_folder_name, new_name)
    assert b_page.is_new_name_appear(new_name), "Folder doesn't renamed"
    b_page.rename_folder(new_name, get_default_folder_name)


@allure.story("Test adding a film to a folder")
@allure.title("Verify adding a film to a folder")
@allure.description("This test verifies the ability to add a film to a folder in the bookmarks.")
@allure.tag("Bookmarks", "Films")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke_cases
def test_add_film(open_main_page, open_bookmarks_page, get_film, get_default_folder_name):
    b_page = open_bookmarks_page
    films_before = b_page.check_films_count_in_folder(get_default_folder_name)
    m_page = open_main_page
    m_page.search_cinema(get_film)
    m_page.click_on_random_film()
    b_page.add_film_to_folder(get_default_folder_name)
    assert b_page.check_films_count_in_folder(get_default_folder_name) == films_before + 1, "Cinema doesn't added"


@allure.story("Test changing a film's folder")
@allure.title("Verify changing a film's folder")
@allure.description("This test verifies the ability to change a film's folder in the bookmarks.")
@allure.tag("Bookmarks", "Films")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression_cases
def test_change_film_folder(open_bookmarks_page, get_default_folder_name):
    b_page = open_bookmarks_page
    to_folder = "Move here"
    before_from = b_page.check_films_count_in_folder(get_default_folder_name)
    before_to = b_page.check_films_count_in_folder(to_folder)
    b_page.change_folder(get_default_folder_name, to_folder)
    assert b_page.check_films_count_in_folder(get_default_folder_name) == before_from - 1
    assert b_page.check_films_count_in_folder(to_folder) == before_to + 1
