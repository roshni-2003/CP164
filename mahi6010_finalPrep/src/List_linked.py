"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2018-06-25"
-------------------------------------------------------
"""
from copy import deepcopy


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
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
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
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if self._front is None:
            new_node = _List_Node(value, None)
            self._front = new_node
            self._rear = new_node
        else:
            self._front = _List_Node(value, self._front)
        
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
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        new_node = _List_Node(value, None)
        
        if self._rear is None:
            # List is empty
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
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
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if i > self._count: # Append
            self.append(value)
        elif i < -self._count or i == 0:  # Prepend
            self.prepend(value)
        else:   # Just insert at i
            if i > 0:
                to_insert_at = i
            else:
                to_insert_at = self._count + i
            
            index = 0
            current = self._front
            previous = None
            while index < to_insert_at:
                previous = current
                current = current._next
                index += 1
            # Inserting between previous and current
            new_node = _List_Node(value, current)
            previous._next = new_node
            
            self._count += 1
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        # your code here
        current = self._front
        index = 0
        previous = None
        while not current is None and current._value != key:
            previous = current
            current = current._next
            index += 1
        if current is None:
            index = -1
        return previous, current, index

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search_r(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        index = 0
        if current is None:
            # Empty list
            index = -1
        else:
            previous, current, index = self._linear_search_r_aux(key, previous, current, index)
        return previous, current, index
    
    def _linear_search_r_aux(self, key, previous, current, index):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        if current is None:
            index = -1
        elif current._value != key:
            index += 1
            previous, current, index = self._linear_search_r_aux(key, current, current._next, index)
            
        return previous, current, index
    
    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        previous, current, index = self._linear_search(key)
        if self._count == 0:
            # Empty list
            value = None
        elif previous is None:
            # One element
            value = current._value
            self._count = 0
            self._front = None
            self._rear = None
        elif index == -1:
            # Key not found
            value = None
        else:
            # Key found, more than one element
            value = current._value
            previous._next = current._next
            current._next = None
            self._count -= 1
        return deepcopy(value)

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        # your code here
        value = self._front._value
        self._front = self._front._next
        # Added after assignment marked
        self._count -= 1
        # END OF ADDITIONS
        return deepcopy(value)

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        current = self._front
        
        while current is not None:
            p, c, _ = self._linear_search(key)
            if c is not None:
                if c is self._front:
                    self._front = self._front._next
                    if self._count == 1:
                        self._rear = None
                elif c is self._rear and c is self._front:
                    self._front = None
                    self._rear = None
                else:
                    p._next = c._next
                self._count -= 1
            current = current._next
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        previous, current, index = self._linear_search(key)
        value = current._value
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        # your code here
        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        # your code here
        previous, current, i = self._linear_search(key)
        
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # your code here
        if i > 0:
            iter_to = i
        elif i == 0:
            iter_to = 0
        else:
            iter_to = self._count + i
        index = 0
        current = self._front
        while index < iter_to:
            current = current._next
            index += 1
        return deepcopy(current._value)

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # your code here
        if i == 0:
            iter_to = 0
        elif i > 0:
            iter_to = i 
        else:
            iter_to = self._count + i
        index = 0
        current = self._front
        while index < iter_to:
            current = current._next
            index += 1
        current._value = deepcopy(value)
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        _, _, index = self._linear_search(key)
        
        return index != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        current = self._front
        max_data = current._value
        while not current is None:
            if current._value > max_data:
                max_data = current._value
            current = current._next
        return deepcopy(max_data)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        current = self._front
        min_data = self._front._value
        while not current is None:
            if current._value < min_data:
                min_data = current._value
            current = current._next
        return deepcopy(min_data)

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        # your code here
        current = self._front
        number = 0
        while not current is None:
            if current._value == key:
                number += 1
            current = current._next
        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        # your code here
        # From the Lab 7 webpage
        new_front = None

        if self._front is not None:
            # set up _rear
            self._rear = self._front
            self._front = self._front._next
            self._rear._next = None
            new_front = self._rear

        while self._front is not None:
            temp = self._front._next
            self._front._next = new_front
            new_front = self._front
            self._front = temp
        self._front = new_front
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        # your code here
        new_front = None
        if self._front is not None:
            # Set up _rear
            self._rear = self._front
            self._front = self._front._next
            self._rear._next = None
            new_front = self._rear
            
        self._reverse_r_aux(new_front)
        return

    def _reverse_r_aux(self, new_front):
        """
        """
        if self._front is not None:
            temp = self._front._next
            self._front._next = new_front
            new_front = self._front
            self._front = self._reverse_r_aux(temp)
        self._front = new_front
        return new_front

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: sl.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        current = self._front
        previous = None
        already_seen = []
        
        while current is not None:
            if current._value not in already_seen:
                already_seen.append(current._value)
                previous = current
            else:
                previous._next = current._next
                self._count -= 1
            current = current._next
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if i[0] < 0:
                # index is negative
                n = self._count + i[0]
            else:
                n = i[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

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
        Returns:
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

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (iterative version)
        Use: b = lst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """
        # your code here
        """
        current1 = self._front
        current2 = other._front
        # Sizes have to match. If not, then not identical
        identical = self._count == other._count
        
        while identical and current1 is not None:
            value1 = current1._value
            value2 = current2._value
            if not value1 == value2:
                identical = False
            current1 = current1._next
            current2 = current2._next
        """
        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            other = other._front

            while source_node is not None and source_node._value == other._value:
                source_node = source_node._next
                other = other._next

            identical = source_node is None
        return identical

    def is_identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        # your code here
        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            other_node = other._front
            source_node, other_node = self._is_identical_r_aux(source_node, other_node)
            identical = source_node is None
        return identical

    def _is_identical_r_aux(self, source_node, other_node):
        """
        """
        #print("Source: {}".format(source_node._value))
        #print("Other: {}".format(other_node._value))
        if source_node is not None and source_node._value == other_node._value:
            source_node, other_node = self._is_identical_r_aux(source_node._next, other_node._next)
        return source_node, other_node
    
    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with < 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        target1 = List()
        target2 = List()
        
        # Nothing to split if no nodes
        if self._front is not None:
            
            current = self._front
            previous = None
            
            # Create a new node to start target1 off
            new_node = _List_Node(current._value, None)
            target1._front = new_node
            target1._rear = new_node
            target1._count += 1
            previous = current
            current = current._next
            previous._next = None
            self._count -= 1
            
            # This floors so access 2nd half as this onwards
            middle = self._count // 2 - 1
            
            # If there was only one node in this List, we are done
            if self._count > 0:
                index = 0
                # Go up to, but not including, the middle of the list
                while index <= middle:
                    target1._rear._next = current
                    target1._rear = current
                    previous = current
                    current = current._next
                    previous._next = None
                    self._count -= 1
                    index += 1
                    target1._count += 1
            
                if self._front is not None:
                    # Create a new node to start target2 off
                    new_node2 = _List_Node(current._value, None)
                    target2._front = new_node2
                    target2._rear = new_node2
                    target2._count = 1
                    previous = current
                    current = current._next
                    previous._next = None
                    self._count -= 1
                    
                    # Go to the end of the List
                    while current is not None:
                        previous = current
                        target2._rear._next = current
                        target2._rear = current
                        current = current._next
                        previous._next = None
                        self._count -= 1
                        target2._count += 1
                    
            # Feel like this is a bit forced..
            self._front = None
            self._rear = None
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        # your code here
        """
        target1 = List()
        target2 = List()
        
        current = self._front
        previous = None
        
        index = 0
        target1_front_set = False
        target2_front_set = False
        
        while current is not None:
            previous = current
            
            if index % 2 == 0:
                # Runs once to start off target1
                if not target1_front_set:
                    new_node = _List_Node(current._value, None)
                    target1._front = new_node
                    target1._rear = new_node
                    target1._count = 1
                    target1_front_set = True
                else:
                    target1._rear._next = current
                    target1._rear = current
            else:
                # Runs once to start off target2
                if not target2_front_set:
                    new_node = _List_Node(current._value, None)
                    target2._front = new_node
                    target2._rear = new_node
                    target2._count = 1
                    target2_front_set = True
                else:
                    target2._rear._next = current
                    target2._rear = current
            current = current._next
            previous._next = None
            self._count -= 1
            index += 1
            
        # Again with the forcing of the emptiness..
        # Only b/c I always get stuck with self._front
        # Remaining in the list
        self._front = None
        self._rear = None
        """
        target1 = List()
        target2 = List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        # your code here
        even = List()
        odd = List()
        left = True
        even, odd, node, left = self._split_alt_r_aux(even, odd, self._front, left)
        return even, odd

    def _split_alt_r_aux(self, even, odd, node, left):
        """
        """
        #print("Even: {}\nOdd: {}\nNode: {}\nLeft: {}".format(even, odd, node, left))
        if node is not None:
            if left:
                even._move_front_to_rear(self)
            else:
                odd._move_front_to_rear(self)
            left = not left
            even, odd, node, left = self._split_alt_r_aux(even, odd, node._next, left)
        return even, odd, node, left

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        # The following is from the Lab 7 task page
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    #self.append(value)
                    new_node = _List_Node(value, None)
                    if self._rear is None:
                        self._front = new_node
                        self._rear = new_node
                    else:
                        self._rear._next = new_node
                        self._rear = new_node
                    self._count += 1

            source1_node = source1_node._next
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        source1_node = source1._front
        self._intersection_r_aux(source1_node, source2)
        return

    def _intersection_r_aux(self, source1_node, source2):
        """
        """
        if source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)
            if current is not None:
                _, current, _ = self._linear_search(value)
                if current is None:
                    self.append(value)
            source1_node = self._intersection_r_aux(source1_node._next, source2)
        return source1_node

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        # From the Lab 7 webpage
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                #self.append(value)
                new_node = _List_Node(value, None)
                if self._rear is None:
                    self._rear = new_node
                    self._front = new_node
                else:
                    self._rear._next = new_node
                    self._rear = new_node
                self._count += 1
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                #self.append(value)
                new_node = _List_Node(value, None)
                """ Previous (what was marked)
                self._rear._next = new_node
                self._rear = new_node
                self._count += 1
                """
                # Added after assignment marked (fixes AttributeError)
                if self._front is None:
                    self._rear = new_node
                    self._front = new_node
                else:
                    self._rear._next = new_node
                    self._rear = new_node
                # END OF ADDITIONS
                
            source2_node = source2_node._next
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        source1_node = source1._front
        self._union_r_aux(source1_node)
        source2_node = source2._front
        self._union_r_aux(source2_node)
        return

    def _union_r_aux(self, source_node):
        """
        """
        if source_node is not None:
            value = source_node._value
            _, current, _ = self._linear_search(value)
            if current is None:
                self.append(value)
            source_node = self._union_r_aux(source_node._next)
        return source_node

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = lst.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        # your code here
        new_list = List()
        current = self._front
        
        # Set up list
        new_node = _List_Node(current._value, None)
        new_list._front = new_node
        new_list._rear = new_node
        new_list._count = 1
        
        new_current = new_list._rear
        current = current._next
        while current is not None:
            new_node = _List_Node(current._value, None)
            new_current._next = new_node
            new_current = new_node
            new_list._count += 1
            current = current._next
            
        return new_list

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        return

    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        # your code here
        return

    def _move_front(self, rs):
        """
        -------------------------------------------------------
        Moves the front node from the rs List to the front
        of the current List. Private helper method.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the rs List and
            its count is updated. The rs List front and count are updated.
        -------------------------------------------------------
        """
        assert rs._front is not None, \
            "Cannot move the front of an empty List"

        # your code here
        
        if self._front is None:
            new_node = _List_Node(rs._front._value, None)
            self._front = new_node
            self._rear = new_node
        else:
            self._front = _List_Node(rs._front._value, self._front)
        
        self._count += 1
        if rs._count == 1:
            rs._front = None
            rs._rear = None
            rs._count = 0
        else:
            rs._front = rs._front._next
            rs._count -= 1
        return

    def _move_front_to_rear(self, rs):
        assert rs._front is not None, \
            "Cannot move the front of an empty List"
        new_node = _List_Node(rs._front._value, None)
        if self._front is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        
        self._count += 1
        if rs._count == 1:
            rs._front = None
            rs._rear = None
            rs._count = 0
        else:
            rs._front = rs._front._next
            rs._count -= 1
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        
        # Used if one of the Lists are empty
        main_node = None
        
        if source1._front is None and source2._front is not None:
            # Source1 is empty, so only using source2
            new_node = _List_Node(source2._front._value, None)
            if self._rear is None:
                self._rear = new_node
                self._front = new_node
            else:
                self._rear._next = new_node
                self._rear = new_node
            self._count += 1
            source2._front = source2._front._next
            source2._count -= 1
            main_node = source2
        elif source2._front is None and source1._front is not None:
            # Source2 is empty, so only using source1
            new_node = _List_Node(source1._front._value, None)
            if self._rear is None:
                self._rear = new_node
                self._front = new_node
            else:
                self._rear._next = new_node
                self._rear = new_node
            self._count += 1
            source1._front = source1._front._next
            source1._count -= 1
            main_node = source1
        elif source1._front is not None and source2._front is not None:
            # Both have nodes, start interlacing
            new_node = _List_Node(source1._front._value, None)
            if self._rear is None:
                self._rear = new_node
                self._front = new_node
            else:
                self._rear._next = new_node
                self._rear = new_node
            self._count += 1
            source1._count -= 1
            # Update the front
            source1._front = source1._front._next
            
            new_node = _List_Node(source2._front._value, None)
            if self._rear is None:
                self._rear = new_node
                self._front = new_node
            else:
                self._rear._next = new_node
                self._rear = new_node
            self._count += 1
            source2._count -= 1
            source2._front = source2._front._next
            
        # Both source1 and source2 have nodes
        if main_node is None:
            
            source1_node = source1._front
            source2_node = source2._front
            
            while source1_node is not None:
                self._rear._next = source1_node
                self._rear = source1_node
                source1_prev = source1_node
                source1_node = source1_node._next
                source1_prev = None
                source1._count -= 1
                self._count += 1
                if source2_node is not None:
                    self._rear._next = source2_node
                    self._rear = source2_node
                    source2_prev = source2_node
                    source2_node = source2_node._next
                    source2_prev = None
                    source2._count -= 1
                    self._count += 1
            source1._front = None
            source1._rear = None
            source2._front = None
            source2._rear = None
        else:
            # One of the sources don't have nodes, use main_node which
            # represents the non-empty list
            current = main_node._front
            previous = None
            
            while current is not None:
                self._rear._next = current
                self._rear = current
                previous = current
                current = current._next
                previous._next = None
                main_node._count -= 1
                self._count += 1
            
            main_node._front = None
            main_node._rear = None
            
                    
        
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
