# test_schema_validation.py

import requests
from jsonschema import validate

def test_user_schema():

    response = requests.get(
        "https://dummyjson.com/users/1"
    )

    data = response.json()

    schema = {
        "type": "object",
        "properties": {
            "data": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"}
                },
                "required": [
                    "id",
                    "email",
                    "first_name",
                    "last_name",
                    "avatar"
                ]
            }
        }
    }

    validate(
        instance=data,
        schema=schema
    )
