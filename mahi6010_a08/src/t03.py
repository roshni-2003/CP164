"""
------------------------------------------------------------------------
Assignment 8, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-22
------------------------------------------------------------------------
"""
from functions import do_comparisons, comparison_total, \
letter_table
from Letter import Letter
from BST_linked import BST
from t02 import DATA3

bst_3 = BST()

for data in DATA3:
    letter = Letter(data)
    bst_3.insert(letter)

fh = open('otoos610.txt', 'r')
do_comparisons(fh, bst_3)    

total_3 = comparison_total(bst_3)

print("DATA3 BST: {}".format(total_3))

letter_table(bst_3)