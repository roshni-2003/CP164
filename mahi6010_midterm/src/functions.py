"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Priority_Queue_array import Priority_Queue
from List_array import List

# Constants
OPERATORS = ('*', '/', '+', '-')


def pq_triage(source, key):
    """
    -------------------------------------------------------
    Removes all values from source that have a priority
    less than key.
    Use: pq_triage(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a key value (?)
    Returns​‌‌‌‌​​​‌:
        None
    -------------------------------------------------------
    """

    for i in source:
        if i < key:
            source.pop(key)
    return


def purge(source, key):
    """
    -------------------------------------------------------
    Finds and removes all values in source that match key.
    Use: purge(source, key)
    -------------------------------------------------------
    Parameters:
        source - a List of values (List)
        key - a data element (?)
    Returns​‌‌‌‌​​​‌:
        None
    -------------------------------------------------------
    """
    x = source.find(key)
    if x is not None:
        for i in range(len(source) - 1, -1, -1):
            if source[i] == key:
                source.pop(i)
        return


def eval_expression(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = eval_expression(string)
    -------------------------------------------------------
    Parameters:
        string - the space-separted postfix string to evaluate (str)
    Returns​‌‌‌‌​​​‌:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    lis = list()
    for symbol in string:
        if symbol in "0123456789":
            lis.append(int(symbol))
            plus = None
        elif not lis.is_empty():
            if symbol == "+":
                plus = lis.remove() + lis.remove()
            elif symbol == "-":
                plus = lis.remove() - lis.remove()
            elif symbol == "*":
                plus = lis.remove() * lis.remove()
            elif symbol == "/":
                plus = lis.remove() / lis.remove()
        if plus is not None:
            lis.append(plus)
        else:
            raise Exception("unknown value %s" % symbol)
    return lis.remove()
