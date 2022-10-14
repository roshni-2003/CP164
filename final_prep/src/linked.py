"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-04-14"
-------------------------------------------------------
"""
from copy import deepcopy


class _List_Node:
    def __init__(self, value, next_):
        self._value = deepcopy(value)
        self._next = next_


class List:
    def __init__(self):
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        return self._front is None

    def __len__(self):
        return self._count

    def append(self, value):
        node = _List_Node(value, None)
        if self._front is None:
            self._front = node

        else:
            self._rear._next = node
        self._rear = node
        self._count += 1
        return

    def peek(self, i):
        current = self._front
        if i < 0:
            i = self._count + 1
        j = 0

        while j < i:
            current = current._next
            j += 1
            value = deepcopy(current._value)
            return value

    def return_values(self):
        values = []
        current = self._front
        while current:
            values.append(current._value)
            current = current._next
        return values
