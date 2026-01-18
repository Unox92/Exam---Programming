"""
Task 7

This file contains two functions:
1) sum_of_five
2) comparison
"""

def sum_of_five(a=1, b=2, c=3, d=4, e=5):
    """
    Returns the sum of five integer values.
    Default values are 1, 2, 3, 4, and 5.
    """
    return a + b + c + d + e


def comparison(x, y):
    """
    Compares two integers and returns a string
    describing their relationship.
    """
    if x < y:
        return "smaller than"
    elif x > y:
        return "greater than"
    else:
        return "equal to"