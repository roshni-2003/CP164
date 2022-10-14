"""
------------------------------------------------------------------------
Lab 8, Task 6 - decode_morse
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-11
------------------------------------------------------------------------
"""
from BST_linked import BST
from morse import decode_morse, fill_code_bst, data1

code_bst = BST()
values = data1

fill_code_bst(code_bst, values)

morse = """.... . .-.. .-.. --- 
-- -.-- 
-. .- -- . 
.. ... 
-. .. -.-. -.- 
-- .. .-.. .-.. ..."""

print("\nTest with BST as None")
text = decode_morse(None, morse)
print("Morse: {}".format(morse))
print("Text: {}".format(text))

print("\nTest with code as None")
text = text = decode_morse(code_bst, None)
print("Morse: {}".format(None))
print("Text: {}".format(text))

print("\nTest with code as empty string")
text = decode_morse(None, "")
print("Morse: {}".format(""))
print("Text: {}".format(text))

print("\nTest with valid BST and Morse code")
text = decode_morse(code_bst, morse)
print("Morse: {}".format(morse))
print("Text: {}".format(text))