#!/usr/bin/env python3
"""
    encrypting user passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string.

    Args:
        password (str): password

    Returns:
        bytes: encryption password
    """
    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks whether password is valid

    Args:
        hashed_password (bytes): hash
        password (str): password

    Returns:
        bool: true or false
    """
    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)
