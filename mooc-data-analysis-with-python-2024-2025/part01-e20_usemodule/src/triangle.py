# Enter you module contents here

"""Computes the hypotenuse and area of right-angled triangle"""
__author__ = "Amit Srivastava"
__version__ = "1.0"

from math import sqrt


def hypotenuse(a, b):
    """Computes the hypotenuse of right-angled triangle when given length of two other sides"""
    return sqrt(a**2 + b**2)


def area(a, b):
    """Computes the area of right-angled triangle when given length of two sides perpendicular to each other"""
    return 0.5 * a * b
