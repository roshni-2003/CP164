"""
------------------------------------------------------------------------
Implementation of a Circular Queue
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-21
------------------------------------------------------------------------
"""
from copy import deepcopy

class Queue():
    
    def __init__(self, max_size):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: cq = Queue(max_size)
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert max_size > 0, "Queue size must be > 0"

        self._max_size = max_size
        self._values = [None] * self._max_size
        self._front = 0
        self._rear = 0
        self._count = 0
        
    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a new value to the rear of the Queue - fails if the Queue 
        is full.
        Use: q.insert(value)
        -------------------------------------------------------
        Parameters:
            value - 
        -------------------------------------------------------
        """
        return
    
    def remove(self):
        return
    
    def peek(self):
        return
    
    def is_empty(self):
        return
    
    def is_full(self):
        return
    
    def length(self):
        return self._count