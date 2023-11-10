from http import HTTPStatus


def test_get_users(set_up, get_headers):
    api = set_up
    response = api.get_all_users(get_headers)
    assert response.status_code == HTTPStatus.OK


def test_get_user(set_up, get_headers, get_random_user):
    api = set_up
    user_id = get_random_user
    response = api.get_one_user(user_id, get_headers)
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['id'] == user_id


def test_post_new_user(set_up, get_fake_user_payload, get_headers):
    api = set_up
    payload = get_fake_user_payload
    resp = api.post_new_user(payload, get_headers)
    assert resp.status_code == HTTPStatus.CREATED
    data = resp.json()
    assert data['name'] == payload['name']


def test_update_user(set_up, get_random_user, random_change, get_headers):
    api = set_up
    payload = random_change
    resp = api.patch_user(get_random_user, payload, get_headers)
    assert resp.status_code == HTTPStatus.OK
    data = resp.json()
    assert data['name'] == payload['name']


def test_delete_user(set_up, get_random_user, get_headers):
    api = set_up
    resp = api.delete_user(get_random_user, get_headers)
    assert resp.status_code == HTTPStatus.NO_CONTENT


def test_put_user(set_up, get_random_user, get_fake_user_payload, get_headers):
    api = set_up
    resp = api.put_user(get_random_user, get_fake_user_payload, get_headers)
    assert resp.status_code == HTTPStatus.OK


def test_not_found(set_up, get_headers):
    api = set_up
    user_id = 0
    response = api.get_one_user(user_id, get_headers)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_bad_request(set_up, get_random_user, get_fake_user_payload, get_headers):
    api = set_up
    payloads = get_fake_user_payload
    resp = api.bad_patch_user(get_random_user, payloads, get_headers)
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_too_many_requests(set_up, get_headers):
    api = set_up
    resp = api.too_many_requests(get_headers)
    assert resp.status_code == 429


def test_not_posted(set_up, get_headers, random_change):
    api = set_up
    resp = api.post_new_user(random_change, get_headers)
    assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
