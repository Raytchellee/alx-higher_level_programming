#!/usr/bin/python3
"""Adda an attribute to a function if possible"""


def add_attribute(obj, att, value):
    """Adds att to a function if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
