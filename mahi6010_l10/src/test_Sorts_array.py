"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2019-02-18"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []
    for i in range(SIZE):
        num = Number(i)
        values.append(num)
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []
    for i in range(SIZE - 1, -1, -1):
        num = Number(i)
        values.append(num)
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    # your code here
    arrays = [[None for i in range(SIZE)] for j in range(TESTS)]
    for i in range(TESTS):
        for j in range(SIZE):
            rand = random.randint(0, XRANGE)
            num = Number(rand)
            arrays[i][j] = num
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    Sorts.swaps = 0
    Number.comparisons = 0
    sorted_list = create_sorted()
    print("{}".format(title),end='')
    func(sorted_list)
    comparisons_sorted = Number.comparisons
    num_swaps_sorted = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0
    
    reversed_list = create_reversed()
    func(reversed_list)
    comparisons_reversed = Number.comparisons
    num_swaps_reversed = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0
    
    random_list = create_randoms()
    total_comparisons_random = 0
    for _list in random_list:
        func(_list)
        total_comparisons_random += Number.comparisons
        Number.comparisons = 0
    average_comparisons_random = total_comparisons_random / len(random_list)
    avg_swaps_random = Sorts.swaps / len(random_list)
    Sorts.swaps = 0
    
    print("\t{:<8.0f} {:<8.0f} {:<8.0f}\t{:<8.0f} {:<8.0f} {:<8.0f}".format(comparisons_sorted, comparisons_reversed, \
                                                            average_comparisons_random, num_swaps_sorted, \
                                                            num_swaps_reversed, avg_swaps_random))
    return
