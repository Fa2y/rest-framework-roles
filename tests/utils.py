from rest_framework.test import APIClient
_client = APIClient()


def get_response(user, get=None, post=None):
    """ Check return statuses """
    assert get or post
    if user.is_anonymous:
        _client.force_authenticate()
    else:
        _client.force_authenticate(user)
    if get:
        return _client.get(get)
    else:
        return _client.post(post)


def assert_allowed(user, get=None, post=None, expected_status=(200, 201)):
    response = get_response(user, get, post)
    if response.status_code not in expected_status:
        raise AssertionError(f"'{user}' should be allowed, but got '{response.status_code}'")


def assert_disallowed(user, get=None, post=None, expected_status=(403,)):
    response = get_response(user, get, post)
    if response.status_code not in expected_status:
        raise AssertionError(f"'{user}' should be forbidden, but got '{response.status_code}'")


# ------------------------------------------------------------------------------