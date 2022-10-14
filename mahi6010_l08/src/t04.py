"""
------------------------------------------------------------------------
Lab 8, Task 4 - fill_code_bst
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-11
------------------------------------------------------------------------
"""
from BST_linked import BST
from morse import fill_code_bst, data1

code_bst = BST()
values = data1

fill_code_bst(code_bst, values)

for code in code_bst:
    print(code)