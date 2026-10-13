import requests


def test_token_exists():

    token = "fake_token"

    assert token is not None
    assert len(token) > 0