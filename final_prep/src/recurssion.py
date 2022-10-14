"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-04-14"
-------------------------------------------------------
"""


def fibonacci(n):
    if n == 1 or n == 2:  # base case
        result = 1

    else:  # recursive case
        result = fibonacci(n - 1) + fibonacci(n - 2)

    return result
