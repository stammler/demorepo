"""
This module contains utility functions for the main module.
"""

import numbers


def isnumeric(a):
    """
    Function checks if input is a number.

    Parameters
    ----------
    a : any
        Input to checked

    Returns
    -------
    is_number : boolean
        Is `True` if `a` is a number. Return `False` else.
    """
    return isinstance(a, numbers.Number)
