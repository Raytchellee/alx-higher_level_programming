#!/usr/bin/python3
"""A rebel class of int"""


class MyInt(int):
    """a rebel class on instance int"""

    def __eq__(self, other):
        """reverses equality"""
        if isinstance(self, type(other)):
            return False

    def __ne__(self, other):
        """reverses not equal"""
        if isinstance(self, type(other)):
            return True
