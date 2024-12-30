import jwt
import os
from time import time
from apiflask import HTTPTokenAuth

auth = HTTPTokenAuth(scheme="Bearer")

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"


def create_access_token(data: dict):
    payload = data.copy()
    payload.update({"exp": int(time()) + 3600})
    encoded_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_token


@auth.verify_token
def verify_token(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return False
    if "username" in data:
        return data["username"]
