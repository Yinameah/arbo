#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class IdMan(object):
    _is_instance = False
    _instance = None

    # Remimplement new to have only one instance of IdMan
    def __new__(cls, *args, **kwargs):
        if cls._is_instance :
            return cls._instance
        else:
            cls._is_instance = True
            obj = super().__new__(cls)
            cls._instance = obj
            return obj

    def __init__(self):
        pass
