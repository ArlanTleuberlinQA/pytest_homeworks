import configparser
import json
from HomeWork15.constants import ROOT_PATH

_abs_path = f'{ROOT_PATH}/configs/app_config.ini'
_config = configparser.RawConfigParser()
_config.read(_abs_path)
_abs_path_j = f'{ROOT_PATH}/configs/app_config.json'
with open(_abs_path_j, 'r') as config_file:
    config_data = json.load(config_file)


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
    test_email = _config.get('user_data', 'test_mail')


class AppConfigJson:
    url = config_data['app_data']['url']
    login = config_data['user_data']['login']
    password = config_data['user_data']['password']
    browser_id = config_data['browser_data']['browser_id']
    bad_password = config_data['user_data']['bad_password']
    cinema = config_data['search_data']['film']
    serial = config_data['app_data']['serial_url']
    email = config_data['user_data']['mail']
    test_email = config_data['user_data']['test_mail']
    api_url = config_data['api_data']['base_url']
    api_token = config_data['api_data']['access_token']
