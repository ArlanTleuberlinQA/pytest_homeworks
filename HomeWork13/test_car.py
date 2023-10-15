import pytest


@pytest.mark.positive_case
def test_engine_start(get_new_car):
    new_car = get_new_car
    assert new_car.start_engine() == "Engine started."


@pytest.mark.positive_case
def test_engine_already_started(get_new_car):
    new_car = get_new_car
    new_car.start_engine()
    assert new_car.start_engine() == "Engine is already running."


@pytest.mark.positive_case
def test_engine_stop(get_new_car):
    new_car = get_new_car
    new_car.start_engine()
    assert new_car.stop_engine() == "Engine stopped."


@pytest.mark.positive_case
def test_engine_already_stopped(get_new_car):
    new_car = get_new_car
    assert new_car.stop_engine() == "Engine is already off."


@pytest.mark.positive_case
def test_driving(get_new_car, get_miles_to_drive):
    new_car = get_new_car
    new_car.start_engine()
    miles_to_drive = get_miles_to_drive
    assert new_car.drive(miles_to_drive) == f"Driving {miles_to_drive} miles."


@pytest.mark.positive_case
def test_miles_limit_without_drive(get_new_car, get_miles_limit):
    new_car = get_new_car
    assert new_car.miles_limit == get_miles_limit


@pytest.mark.positive_case
def test_miles_max(get_new_car):
    new_car = get_new_car
    new_car.start_engine()
    assert new_car.drive(201) == f"The miles limit has been exceeded"


@pytest.mark.positive_case
def test_cant_drive(get_new_car, get_miles_to_drive):
    new_car = get_new_car
    miles_to_drive = get_miles_to_drive
    assert new_car.drive(miles_to_drive) == "Cannot drive. Engine is off."


@pytest.mark.negative_case
def test_drive_with_non_integer_miles(get_new_car):
    car = get_new_car
    car.start_engine()
    with pytest.raises(TypeError):
        car.drive("50")


@pytest.mark.negative_case
def test_incorrect_model(get_incorrect_car):
    with pytest.raises(TypeError):
        get_incorrect_car()


@pytest.mark.positive_case
def test_miles_limit_change_with_drive(get_miles_to_drive, get_new_car, get_miles_limit):
    car = get_new_car
    car.start_engine()
    car.drive(get_miles_to_drive)
    assert car.miles_limit == get_miles_limit - get_miles_to_drive
