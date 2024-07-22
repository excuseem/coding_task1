import jwt
import time

from proxy.jwt_utils import create_jwt_token
from proxy.tests.test_data import TEST_PAYLOAD


def test_create_jwt_token():
    token = create_jwt_token(TEST_PAYLOAD)
    decoded = jwt.decode(token, options={"verify_signature": False})
    assert decoded["payload"] == TEST_PAYLOAD
    assert abs(decoded["iat"] - int(time.time())) < 10
    assert "jti" in decoded
