from api.api_auth import login


def test_login_api():

    response = login(
        "emilys",
        "emilyspass"
    )

    assert response.status_code == 200