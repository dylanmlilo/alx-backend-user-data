#!/usr/bin/env python3
""" Module that defines the API authentication """
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """ Manages the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authorithation check """
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        for i in excluded_paths:
            if path[:i.find('*')] in i[:i.find('*')]:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header check"""
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user method"""
        return None

    def session_cookie(self, request=None):
        """ Return a cookie value from a request """
        if request:
            return request.cookies.get(getenv('SESSION_NAME'))
