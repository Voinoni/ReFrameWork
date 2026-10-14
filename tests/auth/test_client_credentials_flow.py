from unittest.mock import patch, Mock
import requests


@patch("requests.post")
def test_client_credentials_flow(mock_post):

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "access_token": "fake_token",
        "token_type": "Bearer"
    }

    mock_post.return_value = mock_response

    response = requests.post(
        "https://api.example.com/oauth/token",
        data={
            "grant_type": "client_credentials"
        }
    )

    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"