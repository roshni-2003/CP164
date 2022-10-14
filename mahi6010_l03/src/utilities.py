"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-05-27"
-------------------------------------------------------
"""
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack, 
    first value in source is on top of stack.
    Use: array_to_stack(s, a)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        element = source[-1]
        stack.push(element)    # Push elem onto stack
        del source[-1]
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and 
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()

    # Test if stack is empty (Expected: TRUE)
    print("Stack contents: ")
    for i in s:
        print(i, end=' ')
    print("\tEmpty? {}".format(s.is_empty()))
    # Load elements from source into Stack
    print(">> Push elements from source onto stack")
    print(">> Num elements to push: {}".format(len(source)))
    for elem in source:
        s.push(elem)

    # Check if the Stack is empty again (T/F depending on source contents)
    print("Stack contents: ")
    for i in s:
        print(i, end=' ')
    print("\tEmpty? {}".format(s.is_empty()))
    # Peek the top of the stack
    top = None
    try:
        top = s.peek()
    except:
        print(">>! Peeked at an empty stack, assertion caught, continuing...")
    # Check if top of stack is the end element of source
    print("Top of stack should be same as end of list")
    if s.is_empty():
        print("List empty so no check")
    else:
        top_same = top == source[-1]
        print("Top same as end of list?")
        print("Top: {}\tEnd of list: {}".format(top, source[-1]))
        print("Same? {}".format(top_same))

    # Testing pop
    try:
        print(">> Pop top of stack")
        popped = s.pop()
        print("Popped value should be same as end of list.\tSame? {}".format(
            popped == source[-1]))
    except:
        print(">>! Popped from an empty stack, exception caught, continuing...")
    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for a in source:
        queue.insert(a)
    for _ in range(len(source) - 1, -1, -1):
        source.pop()


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    print(q.is_empty())
    array_to_queue(q, a)
    value = input("Enter a value: ")
    q.insert(value)
    print(q.peek())
    print(q.remove())
    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        element = source[0]
        pq.insert(element)    # Push elem onto stack
        del source[0]


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    print(pq.is_empty())
    array_to_pq(pq, a)
    value = input("Enter a value: ")
    pq.insert(value)
    print(pq.peek())
    print(pq.remove())

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return
