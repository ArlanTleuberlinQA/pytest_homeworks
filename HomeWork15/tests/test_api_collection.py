from http import HTTPStatus
import allure
import pytest


@pytest.mark.not_ui
@allure.story("Test getting all users")
@allure.title("Verify fetching all users")
@allure.description("This test verifies the ability to fetch all users from the API.")
@allure.tag("API", "Users")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("test-type", "functional")
def test_get_users(set_up, get_headers):
    api = set_up
    response = api.get_all_users(get_headers)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.not_ui
@allure.story("Test getting a single user")
@allure.title("Verify fetching a single user")
@allure.description("This test verifies the ability to fetch a single user from the API.")
@allure.tag("API", "User", "Fetch")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("test-type", "functional")
def test_get_user(set_up, get_headers, get_random_user):
    api = set_up
    user_id = get_random_user
    response = api.get_one_user(user_id, get_headers)
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['id'] == user_id


@pytest.mark.not_ui
@allure.story("Test creating a new user")
@allure.title("Verify creating a new user")
@allure.description("This test verifies the ability to create a new user through the API.")
@allure.tag("API", "Users")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("test-type", "functional")
def test_post_new_user(set_up, get_fake_user_payload, get_headers):
    api = set_up
    payload = get_fake_user_payload
    resp = api.post_new_user(payload, get_headers)
    assert resp.status_code == HTTPStatus.CREATED
    data = resp.json()
    assert data['name'] == payload['name']


@pytest.mark.not_ui
@allure.story("Test updating a user")
@allure.title("Verify updating a user")
@allure.description("This test verifies the ability to update a user's information through the API.")
@allure.tag("API", "Users")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("test-type", "functional")
def test_update_user(set_up, get_random_user, random_change, get_headers):
    api = set_up
    payload = random_change
    resp = api.patch_user(get_random_user, payload, get_headers)
    assert resp.status_code == HTTPStatus.OK
    data = resp.json()
    assert data['name'] == payload['name']


@pytest.mark.not_ui
@allure.story("Test deleting a user")
@allure.title("Verify deleting a user")
@allure.description("This test verifies the ability to delete a user through the API.")
@allure.tag("API", "Users")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("test-type", "functional")
def test_delete_user(set_up, get_random_user, get_headers):
    api = set_up
    resp = api.delete_user(get_random_user, get_headers)
    assert resp.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.not_ui
def test_put_user(set_up, get_random_user, get_fake_user_payload, get_headers):
    api = set_up
    resp = api.put_user(get_random_user, get_fake_user_payload, get_headers)
    assert resp.status_code == HTTPStatus.OK


@pytest.mark.not_ui
@allure.story("Test replacing a user")
@allure.title("Verify replacing a user")
@allure.description("This test verifies the ability to replace a user's information through the API.")
@allure.tag("API", "Users")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("test-type", "functional")
def test_not_found(set_up, get_headers):
    api = set_up
    user_id = 0
    response = api.get_one_user(user_id, get_headers)
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.not_ui
@allure.story("Test making a bad request")
@allure.title("Verify making a bad request")
@allure.description("This test verifies the API's response when making a bad request.")
@allure.tag("API", "Users")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("test-type", "functional")
def test_bad_request(set_up, get_random_user, get_fake_user_payload, get_headers):
    api = set_up
    payloads = get_fake_user_payload
    resp = api.bad_patch_user(get_random_user, payloads, get_headers)
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_too_many_requests(set_up, get_headers):
    api = set_up
    resp = api.too_many_requests(get_headers)
    assert resp.status_code == HTTPStatus.TOO_MANY_REQUESTS


@pytest.mark.not_ui
@allure.story("Test unprocessable entity response")
@allure.title("Verify unprocessable entity response")
@allure.description("This test verifies the API's response when attempting to create a user with invalid data.")
@allure.tag("API", "Users")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("test-type", "functional")
def test_not_posted(set_up, get_headers, random_change):
    api = set_up
    resp = api.post_new_user(random_change, get_headers)
    assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
