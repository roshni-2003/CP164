"""
------------------------------------------------------------------------
Implementation of various sorts in lecture
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-20
------------------------------------------------------------------------
"""

def _swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    return

def insertion_sort_other(a):
    n = len(a)
    
    for i in range(i, n):
        j = i
        
        while j > 0 and a[j - i] > a[j]:
            _swap(a, j - i, j)
            j -= 1
    return

def insertion_sort(a):
    """
    Take a list. Pretend some portion is already sorted (typically
    index 0). Walk through rest of list, grabbing value 
    at each location, swap backwards until in proper place.
    """
    # Assuming first element already sorted "so far"
    for i in range(1, len(a)):
        #j = i - 1
        j = i
        # while j > -1 and a[j] > a[i]:
        while j > 0 and a[j-1] > a[j]:
            # _swap(a, i, j)
            _swap(a, j - 1, j)
            j -= 1
            """
            j -= 1
            i -= 1
            """
    return

def insertion_sort_linked(a):
    """
    """
    unsorted = a._front
    a._front = None
    a._rear = None
    
    while unsorted is not None:
        node = unsorted
        unsorted = unsorted._next
        
        prev = None
        curr = a._front
        
        while curr is not None and node._value >= curr._value:
            prev = curr
            curr = curr._next
            
        if prev is None:
            a._front = node
        else:
            prev._next = node
        node._next = curr
        
        if curr is None:
            a._rear = node
        
    return

a = [3,5,1,9,5,2,8]
insertion_sort(a)
print(a)