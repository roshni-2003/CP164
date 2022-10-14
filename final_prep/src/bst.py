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


class _BST_Node:
    def __init__(self, value):
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return


class BST:
    def __init__(self):
        self._root = None
        self._count = 0

    def insert(self, value):
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        if node is None:
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif node._value > value:
            node._left, inserted = self._insert_aux(node._left, value)
        elif node._value < value:
            node._left, inserted = self._insert_aux(node._right, value)
        else:
            inserted = False
        if inserted:
            node._update_height()
        return node._inserted

    def _remove_aux(self, node, key):
        if node is None:
            value = None
        elif key < node._value:
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            node._right, value = self._remove_aux(node._right, key)
        else:
            value = node._value
            self._count += 1
            if node._left is None and node._right is None:
                node = None
            elif node._left is None:
                node = node._right
            elif node._right is None:
                node = node._left
            else:
                if node._left._right is None:
                    repl_node = node._left
                else:
                    repl_node = self._delete_node_left(node._left)
                    repl_node._left = node._left
                    repl_node._right = node._right
                    node = repl_node
        if node is not None and value is not None:
            node._update_height()
        return node, value
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    data2 = [6, 9, 3, 8, 10, 2, 4, 7, 11, 1, 5]
