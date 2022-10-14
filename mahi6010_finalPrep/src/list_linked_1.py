"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-08-02"
-------------------------------------------------------
"""
from copy import deepcopy
from random import randint


class List:

    def split_th(self):
        """
        -------------------------------------------------------
        Splits source into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = source.split_th()
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        source_length = len(self)
        target1 = List()
        target2 = List()

        print(source_length)

        mid = (source_length // 2) + 1
        num = self._front
        for i in range(1, source_length + 1):
            print(num._value)
            if i <= mid:
                target1.append(num._value)
            else:
                target2.append(num._value)
            num = num._next

        while (self._front is not None):
            temp = self._front
            self._front = self._front._next
            temp = None

        return target1, target2

    def shuffle(self):
        """
        -------------------------------------------------------
        Moves nodes from source to target in random order.
        All data is preserved, order is not. source is empty when
        finished.
        Use: target = source.shuffle()
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            target - a new List with shuffled values from source (List)
        -------------------------------------------------------
        """
        target = List()
        length_list = len(self)
        x = 0
        num = self._front
        while x < length_list:
            index = randint(0, len(self))
            x += 1
            target.insert(index, num._value)
            num = num._next
        while (self._front is not None):
            temp = self._front
            self._front = self._front._next
            temp = None
        return target

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns​​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, self._front)

        if self._rear is None:
            # List is empty - update the rear of the List..
            self._rear = node
        # Update the front of the List.
        self._front = node
        self._count += 1
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns​​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns​​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        # Negative index adjustment.
        if i < 0:
            i = self._count + i

        if i <= 0:
            # Add value to the front of the list
            self.prepend(value)
        elif i >= self._count:
            # Add value to the end of the list
            self.append(value)
        else:
            # Add elsewhere in the list - not to front or rear
            j = 0
            previous = None
            current = self._front

            while j < i:
                # Find the proper location in the List
                previous = current
                current = current._next
                j += 1
            # Create the new node.
            node = _List_Node(value, current)
            previous._next = node
            self._count += 1
        return

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns​​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next
            left._next = right._next
            right._next = temp
            # Update the rear
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
        return

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns​​‌‌​‌​​:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        node._next = self._front
        self._front = node

        if self._rear is None:
            # Target list is empty
            self._rear = node
        self._count += 1
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns​​‌‌​‌​​:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node

        node._next = None
        self._rear = node
        self._count += 1
        return

    def to_set(self):
        """
        -------------------------------------------------------
        Moves nodes from source to target. Values must be unique
        in target. Preserves order of values.
        Use: target = source.to_set()
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            target - a new List with unique values (List)
        -------------------------------------------------------
        """
        target = List()

        while self._front is not None:

            if self._front._value not in target:
                target._move_front_to_rear(self)
            else:
                self._front = self._front._next
        self._count = 0
        self._rear = None
        return target

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns​​‌‌​‌​​:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
