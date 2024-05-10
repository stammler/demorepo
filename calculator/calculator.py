"""
This is the main module that contains the Calculator.
"""

from calculator import utils


class Calculator():
    """
    The main Calculator class, which provides the arithmetic operations.
    """

    def __init__(self):
        pass

    def add(self, a, b):
        """
        Functions adds two numbers
            ``c = a + b``

        Parameters
        ----------
        a : number
            First addend
        b : number
            Second addend

        Returns
        -------
        c : number
            Sum of inputs
        """
        if not (utils.isnumeric(a) and utils.isnumeric(b)):
            raise TypeError("Inputs have to be numbers!")
        else:
            return a + b

    def subtract(self, a, b):
        """
        Functions subtracts one number from another
            ``c = a - b``

        Parameters
        ----------
        a : number
            Minuend
        b : number
            Subtrahend

        Returns
        -------
        c : number
            Difference of inputs
        """
        if not (utils.isnumeric(a) and utils.isnumeric(b)):
            raise TypeError("Inputs have to be numbers!")
        return a - b

    def multiply(self, a, b):
        """
        Functions multiplies two numbers
            ``c = a * b``

        Parameters
        ----------
        a : number
            First factor
        b : number
            Second factor

        Returns
        -------
        c : number
            Product of inputs
        """
        if not (utils.isnumeric(a) and utils.isnumeric(b)):
            raise TypeError("Inputs have to be numbers!")
        return a * b

    def divide(self, a, b):
        """
        Functions divdes one number by another
            ``c = a / b``

        Parameters
        ----------
        a : number
            Dividend
        b : number
            Divisor, must not be zero

        Returns
        -------
        c : number
            Ratio of inputs
        """
        if not (utils.isnumeric(a) and utils.isnumeric(b)):
            raise TypeError("Inputs have to be numbers!")
        if b == 0:
            raise ValueError("Divisor must not be zero!")
        return a / b
