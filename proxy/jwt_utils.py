import jwt
import time
import uuid

from proxy.settings import SECRET, ENCODE_ALGORITHM


def create_jwt_token(payload):
    jwt_payload = {
        "iat": int(time.time()),
        "jti": str(uuid.uuid4()),
        "payload": payload,
    }
    token = jwt.encode(jwt_payload, SECRET, algorithm=ENCODE_ALGORITHM)

    return token
