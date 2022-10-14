"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-21
------------------------------------------------------------------------
"""
from Letter import Letter
def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains 
    the number of comparisons found by searching for that Letter 
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects 
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    file_variable.seek(0)
    lines = file_variable.readlines()
    for line in lines:
        for word in line:
            for letter in word:
                upper_letter = letter.upper()
                if upper_letter in ALPHABET:
                    key = Letter(upper_letter)
                    val = bst.retrieve(key)
    return

def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    inorder = bst.inorder()
    total = 0
    for letter in inorder:
        total += letter.comparisons
    return total

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    print("Letter Count/Percent Table")
    inorder = bst.inorder()
    total = 0
    for letter in inorder:
        total += letter.count
    print("Total Count: {}".format(total))
    
    print("Letter  Count       %")
    print("-"*21)
    for letter in inorder:
        percent = (letter.count / total) * 100
        print("{:>5s} {:>2d} {:>8.2f}%".format(letter.letter, letter.count, percent))