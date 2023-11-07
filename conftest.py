import pytest

from HomeWork15.page_objects.bookmarks_pack.bookmarks_page import BookmarksPage
from HomeWork15.page_objects.login_page_pack.login_page import LoginPage
from HomeWork15.page_objects.main_page_pack.main_page import MainPage
from HomeWork15.page_objects.serial_page_pack.serial_page import SerialPage
from HomeWork15.page_objects.settings_page_pack.settings_page import SettingsPage
from HomeWork15.utilities.config_reader import AppConfigJson
from HomeWork15.utilities.driver_factory import DriverFactory
from faker import Faker
import random


@pytest.fixture
def create_driver():
    driver = DriverFactory(AppConfigJson.browser_id).get_driver()
    driver.maximize_window()
    driver.get(AppConfigJson.url)
    yield driver
    driver.quit()


@pytest.fixture
def create_serial_driver():
    driver = DriverFactory(AppConfigJson.browser_id).get_driver()
    driver.maximize_window()
    driver.get(AppConfigJson.serial)
    yield driver
    driver.quit()


@pytest.fixture
def get_user():
    return AppConfigJson.login, AppConfigJson.password


@pytest.fixture
def get_email():
    return AppConfigJson.email


@pytest.fixture
def get_test_email():
    return AppConfigJson.test_email


@pytest.fixture
def get_password():
    return AppConfigJson.password


@pytest.fixture
def get_test_password():
    return AppConfigJson.bad_password


@pytest.fixture
def get_wrong_user():
    return AppConfigJson.login, AppConfigJson.bad_password


@pytest.fixture
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture
def open_serial_page(create_serial_driver):
    return SerialPage(create_serial_driver)


@pytest.fixture
def open_main_page(create_driver):
    return MainPage(create_driver)


@pytest.fixture
def get_film():
    films_list = AppConfigJson.cinema
    random_film = random.choice(films_list)
    return random_film


@pytest.fixture
def open_settings_page(create_driver, get_user):
    LoginPage(create_driver).do_login(*get_user)
    SettingsPage(create_driver).open_settings()
    return SettingsPage(create_driver)


@pytest.fixture
def open_bookmarks_page(create_driver, get_user):
    LoginPage(create_driver).do_login(*get_user)
    BookmarksPage(create_driver).open_bookmarks()
    return BookmarksPage(create_driver)


@pytest.fixture
def get_default_folder_name():
    return "Test_cinema_folder"


@pytest.fixture
def get_random_folder_name():
    return random.randint(1, 10000)


@pytest.fixture
def get_name_payer():
    fake = Faker()
    name = fake.name()
    return name
