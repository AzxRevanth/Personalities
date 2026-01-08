import bcrypt
from db import users

def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)

def create_user(username: str, password: str):
    if users.find_one({"username": username}):
        return False

    users.insert_one({
        "username": username,
        "password": hash_password(password)
    })
    return True

def authenticate_user(username: str, password: str):
    user = users.find_one({"username": username})
    if not user:
        return False

    return verify_password(password, user["password"])
