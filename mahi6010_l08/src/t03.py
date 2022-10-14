"""
------------------------------------------------------------------------
Lab 8, Task 3 - fill_letter_bst
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-11
------------------------------------------------------------------------
"""
from BST_linked import BST
from morse import fill_letter_bst, data1

letter_bst = BST()
values = data1

fill_letter_bst(letter_bst, values)

for letter in letter_bst:
    print(letter)