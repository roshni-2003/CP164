"""
------------------------------------------------------------------------
Assignment 8, Task 2 - Letter comparisons
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-21
------------------------------------------------------------------------
"""
from functions import comparison_total, do_comparisons, \
letter_table
from BST_linked import BST
from Letter import Letter

bst_1 = BST()
bst_2 = BST()
bst_3 = BST()

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

for data in DATA1:
    letter = Letter(data)
    bst_1.insert(letter)
for data in DATA2:
    letter = Letter(data)
    bst_2.insert(letter)
for data in DATA3:
    letter = Letter(data)
    bst_3.insert(letter)

fh = open('otoos610.txt', 'r')
do_comparisons(fh, bst_1)              
do_comparisons(fh, bst_2)              
do_comparisons(fh, bst_3)    

total_1 = comparison_total(bst_1)
total_2 = comparison_total(bst_2)
total_3 = comparison_total(bst_3)

print("DATA1 BST: {}".format(total_1))
print("DATA2 BST: {}".format(total_2))
print("DATA3 BST: {}".format(total_3))
