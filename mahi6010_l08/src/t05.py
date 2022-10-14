"""
------------------------------------------------------------------------
Lab 8, Task 5 - encode_morse
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-11
------------------------------------------------------------------------
"""
from BST_linked import BST
from morse import encode_morse, fill_letter_bst, data1

letter_bst = BST()
values = data1

fill_letter_bst(letter_bst, values)

text = "Hello, my name is Nick Mills."

morse = encode_morse(letter_bst, text)

print("Text: {}".format(text))
print("Morse: {}".format(morse))