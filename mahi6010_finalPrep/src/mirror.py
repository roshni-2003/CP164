"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-16
------------------------------------------------------------------------
"""
from Stack_array import Stack

CHARS = "abc"
MID = "m"

def mirror(string):
    b = True
    stack = Stack()
    n = len(string)
    i = 0
    
    while b and string[i] != MID:
        if string[i] in CHARS:
            stack.push(string[i])
            i += 1
        else:
            b = False
        
    i += 1  # Skip MID
    
    while b and i < n:
        if stack.is_empty():
            b = False
        else:
            c = stack.pop()
            
            if not c == string[i]:
                b = False
            else:
                i += 1
    
    return b