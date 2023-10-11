import pytest
from car import Car
import random


@pytest.fixture()
def get_new_car():
    new_car = Car('Tesla', '5', 200)
    return new_car


@pytest.fixture()
def get_incorrect_car():
    new_car = Car('Tesla', 5, -200)
    return new_car


@pytest.fixture()
def get_miles_to_drive():
    miles_to_drive = random.randint(1, 199)
    return miles_to_drive


@pytest.fixture()
def get_miles_limit(get_new_car):
    car = get_new_car
    car_limit = car.miles_limit
    return car_limit