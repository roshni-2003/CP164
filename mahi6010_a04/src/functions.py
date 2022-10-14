"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-06-04"
-------------------------------------------------------
"""
from Queue_circular import Queue
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue


def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    target = Queue()
    while not source1.is_empty and not source2.is_empty:
        target.insert(source1.remove())
        target.insert(source2.remove())

    while not source1.is_empty:
        target.insert(source1.remove())
    while not source2.is_empty():
        target.insert(source2.remove())

    return target


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = []
    target2 = []
    for i in range(len(source)):
        elem = source.remove()
        if elem < key:
            target1.append(elem)
        else:
            target2.append(elem)
    return target1, target2
