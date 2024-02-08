#!/usr/bin/env python3
"""
Module documentation
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    psw documentation
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Verify if a given password matches the stored hashed password.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
