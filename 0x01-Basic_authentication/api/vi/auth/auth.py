#!/usr/bin/env python3
""" Module that defines the API authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Manages the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authorithation check"""
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for i in excluded_paths:
            if i.endswith('*'):
                if path.startswith(i[:1]):
                    return False
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ Authorization header check"""
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user method"""
        return None
