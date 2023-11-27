import json

import pytest

from constants import ROOT_PATH
from HomeWork15.page_objects.api_pack.api_collection import UsersApi
from HomeWork15.page_objects.bookmarks_pack.bookmarks_page import BookmarksPage
from HomeWork15.page_objects.login_page_pack.login_page import LoginPage
from HomeWork15.page_objects.main_page_pack.main_page import MainPage
from HomeWork15.page_objects.serial_page_pack.serial_page import SerialPage
from HomeWork15.page_objects.settings_page_pack.settings_page import SettingsPage
from HomeWork15.utilities.config_reader import AppConfigJson
from HomeWork15.utilities.driver_factory import DriverFactory
from faker import Faker
import random
import allure

from HomeWork15.utilities.json_to_dict import DictToClass
from db.sqlite_pack.products_repo import ProductsRepo


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='app_config', help='Choose your env')
    parser.addoption('--hub', action='store', default='false', help='Run test in container Selenoid')
    parser.addoption('--headless', action='store', default='False', help='Run test in headless mode')


@pytest.fixture(scope='session')
def env(request):
    _env_name = request.config.getoption('--env')
    with open(f'{ROOT_PATH}/configs/{_env_name}.json') as f:
        conf_dict = json.loads(f.read())
        return DictToClass(**conf_dict)


@pytest.fixture
def create_driver(env, request):
    driver = DriverFactory(
        browser_id=env.browser_data.get('browse_id', ''),
        hub=eval(request.config.getoption('--hub')),
        headless=eval(request.config.getoption('--headless'))
    ).get_driver()
    driver.maximize_window()
    driver.get(env.app_data.get('url', ''))
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


@pytest.fixture
def get_headers():
    headers = ({
        "Authorization": f"Bearer {AppConfigJson.api_token}",
        "Content-Type": "application/json"
    })
    return headers


@pytest.fixture
def get_base_url():
    base_url = AppConfigJson.api_url
    return base_url


@pytest.fixture
def set_up(get_base_url):
    api = UsersApi(get_base_url)
    return api


@pytest.fixture()
def get_fake_user_payload():
    fake = Faker()
    return {
        "name": fake.name(),
        "email": fake.email(),
        "gender": random.choice(["male", "female"]),
        "status": random.choice(["active", "inactive"])
    }


@pytest.fixture()
def random_change():
    fake = Faker()
    return {
        "name": fake.name(),
        "email": fake.email(),
    }


@pytest.fixture
def get_random_user(set_up, get_headers):
    api = set_up
    response = api.get_all_users(get_headers)
    users = response.json()
    random_user = random.choice(users)
    random_user_id = random_user.get('id')
    return random_user_id


@pytest.fixture(scope='module')
def product_repo(env):
    return ProductsRepo(f"{ROOT_PATH}{env.db_param['path']}")


@pytest.fixture
def get_random_item():
    fake = Faker()
    return {
        "item_id": random.randint(1, 10000),
        "name": random.choice(
            ["Indesit", "Ariston", "Electrolux", "Samsung", "LG", "Toshiba", "Bosch", "Zanussi", "Whirpool"]),
        "category": random.choice(["Steamer", "Slow cooker", "Washing Machine", "Dishwashing", "Refregerator",
                                   "Vacuum cleaner", "Air conditioning", "Heater", "Humidifier", "Oven", "Hob"]),
        "price": float(fake.pyint(10, 6000)),
        "stock_quantity": random.randint(1, 100)}


@pytest.fixture
def get_random_item_id(product_repo):
    db = product_repo
    tab = db.get_all()
    random_item = random.choice(tab)
    random_user_id = random_item[0]
    return random_user_id
