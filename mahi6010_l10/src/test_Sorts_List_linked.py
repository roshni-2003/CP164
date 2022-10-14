"""
-------------------------------------------------------
Tests various linked sorting functions.
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

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

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
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE):
        num = Number(i)
        values.append(num)
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE, -1, -1):
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
        lists - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here
    lists = []
    for i in range(TESTS):
        for _ in range(SIZE):
            inner_list = List()
            rand = random.randint(0, XRANGE)
            num = Number(rand)
            inner_list.append(num)
        lists.append(inner_list)
    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
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
