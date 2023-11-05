import configparser
from HomeWork15.constants import ROOT_PATH

_abs_path = f'{ROOT_PATH}/configs/app_config.ini'
_config = configparser.RawConfigParser()
_config.read(_abs_path)


class AppConfig:
    url = _config.get('app_data', 'url')
    login = _config.get('user_data', 'login')
    password = _config.get('user_data', 'password')
    browser_id = _config.get('browser_data', 'browser_id')
    bad_password = _config.get('user_data', 'bad_password')
    cinema = _config.get('search_data', 'film')
    cinema_list = [str(item) for item in cinema.split(', ')]
    serial = _config.get('app_data', 'serial_url')
    email = _config.get('user_data', 'mail')
    test_email = _config.get('user_data','test_mail')
