"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 A
__updated__ = "2018-10-31"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """

        # Your code here

        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """

        # Your code here

        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        # Your code here
        if self._front is None:
            # First element in Deque
            new_node = _Deque_Node(value, None, None)
            self._front = new_node
            self._rear = new_node
        else:
            new_node = _Deque_Node(value, None, self._front)
            self._front = new_node
        self._count += 1
            
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        # Your code here
        if self._rear is None:
            # First element in Deque
            new_node = _Deque_Node(value, None, None)
            self._rear = new_node
            self._front = new_node
        else:
            new_node = _Deque_Node(value, self._rear, None)
            self._rear._next = new_node
            self._rear = new_node
        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"


        # Your code here
        value = self._front._value
        self._front = self._front._next
        if self._front is not None:
            self._front._prev = None
        self._count -= 1
        if self._count == 0:
            self._front = None
            self._rear = None
        return deepcopy(value)

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"


        # Your code here
        value = self._rear._value
        self._rear = self._rear._prev
        if self._rear is not None:
            self._rear._next = None
        self._count -= 1
        if self._count == 0:
            self._front = None
            self._rear = None
        return deepcopy(value)

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"


        # Your code here
        value = self._front._value
        return deepcopy(value)

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"


        # Your code here
        value = self._rear._value
        return deepcopy(value)

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"

        # Your code here
        
        # Nothing to swap if Deque has <= 1 node
        if self._count > 1:
            # Ensure l comes before r
            if l is self._rear:
                temp = l
                l = r
                r = temp
            if r is self._front:
                temp = r
                r = l
                l = temp
                
            if r._next is not l:
                # r and l not next to each other so use original values
                new_node_l = _Deque_Node(r._value, l._prev, l._next)
                new_node_r = _Deque_Node(l._value, r._prev, r._next)
            else:
                # r and l next to each other so must point to each other
                new_node_l = _Deque_Node(r._value, None, l._next)
                new_node_r = _Deque_Node(l._value, r._prev, new_node_l)
                new_node_l._prev = new_node_r
            if l is self._front:
                # Update self._front and self._front._next._prev
                self._front._next._prev = new_node_l
                self._front = new_node_l
            else:
                # Update l._prev._next and l._next._prev
                l._prev._next = new_node_l
                l._next._prev = new_node_l
            if r is self._rear:
                # Update self._rear and self._rear._prev._next
                self._rear._prev._next = new_node_r
                self._rear = new_node_r
            else:
                # Update r._prev._next and r._next._prev
                r._prev._next = new_node_r
                r._next._prev = new_node_r
            
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
