import os
from datetime import datetime, timedelta

import jwt
from dotenv import load_dotenv

load_dotenv(".env")

secret_key = os.environ["SECRET_KEY"]

algorithm = "HS256"


def create_access_token(data, expires_delta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    access_token = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return access_token


def decode_access_token(data):
    token_data = jwt.decode(data, secret_key, algorithms=algorithm)
    return token_data
