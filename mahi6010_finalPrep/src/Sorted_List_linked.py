"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2019-03-07"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_ListNode)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """

        # your code here

        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """

        # your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """

        # your code here
        if self._front is None:
            new_node = _SL_Node(value, None)
            self._front = new_node
            self._rear = new_node
            self._count += 1
        else:
            current = self._front
            previous = None
            while current is not None and current._value < value:
                previous = current
                current = current._next
                
            new_node = _SL_Node(value, current)
            if current is None:
                # Reached end of list, so this should be the end
                self._rear._next = new_node
                self._rear = new_node
            elif previous is None:
                # Inserting at beginning of list
                self._front = new_node
            else:
                # We're somewhere in the middle, update previous
                # node _next to point to inserted node
                previous._next = new_node
            self._count += 1
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        # your code here
        current = self._front
        previous = None
        index = 0
          
        while current is not None and current._value != key:
            previous = current
            current = current._next
            index += 1
        
        if current is None:
            index = -1
            
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        # your code here
        p, c, i = self._linear_search(key)
        
        if i == -1:
            # Key not found
            value = None
        elif i == self._count:
            # Removing from rear of list, c is rear
            value = c._value
            p._next = None
            self._rear = p
            self._count -= 1
        else:
            # c not None, but p could be None
            if p is None:
                # Removing from front of list
                value = self._front._value
                self._front = self._front._next
                self._count -= 1
            else:
                # Removing from somewhere inside the list
                value = c._value
                p._next = c._next
                c._next = None
                self._count -= 1
                
        # Check if remaining list is empty, update references if needed
        if self._count == 0:
            self._rear = None
            self._front = None
        
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
        if self._count == 1:
            # Removing last node, update front and rear
            self._front = None
            self._rear = None
            self._count -= 1
        else:
            # List not empty after the remove, so just update front
            self._front = self._front._next
            self._count -= 1
            
        return deepcopy(value)

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """

        # your code here

        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        # your code here
        _, c, _ = self._linear_search(key)
        
        if c is None:
            value = None
        else:
            value = c._value
        return deepcopy(value)

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
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
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """

        # your code here
        _, _, i = self._linear_search(key)
        
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

        # your code here
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
        _, _, i = self._linear_search(key)
        
        return i != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        # Since sorted, max will be at end of List
        max = self._rear._value
        return deepcopy(max)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"

        # your code here
        # Since sorted, smallest value will be at front of List
        min = self._front._value
        return deepcopy(min)

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """

        # your code here
        current = self._front
        count = 0
        
        while current is not None and current._value <= key:
            if current._value == key:
                count += 1
            current = current._next
        return count

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
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
                current = current._next
            else:
                previous._next = current._next
                self._count -= 1
                current = current._next
                """
                # Preamble:
                # Since this is a sorted list, duplicates will be side by side
                # Therefore, once a duplicate is found, able to remove the duplicates
                # fairly easily with another loop.
                # Seems redundant however
                temp_current = current
                temp_previous = previous
                while temp_current is not None and temp_current._value == current._value:
                    temp_previous._next = temp_current
                    self._count -= 1
                    temp_current = temp_current._next
                previous._next = temp_current
                if temp_current is None:
                    current = None
                else:
                    current = current._next
                """
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

        if len(i) == 1:

            if i[0] < 0:
                # index is negative
                i[0] = self._count + i[0]
            j = 0

            while j < i[0]:
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

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

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
        source1_node = source1._front
        
        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)
            
            if current is not None:
                # Exists in both lists
                _, current, _ = self._linear_search(value)
                
                if current is None:
                    # Does not appear in this List
                    new_node = _SL_Node(value, None)
                    if self._rear is None:
                        # First node to be added to this list
                        self._front = new_node
                        self._rear = new_node
                        self._count += 1
                    else:
                        # List has nodes, must properly inserted into the List
                        current = self._front
                        previous = None
                        while current is not None and current._value < value:
                            previous = current
                            current = current._next
                            
                        new_node = _SL_Node(value, current)
                        # Reached end of list so add to end
                        if current is None:
                            self._rear._next = new_node
                            self._rear = new_node
                        else:
                            # Somewhere in middle, update references
                            previous._next = new_node
                        self._count += 1
            source1_node = source1_node._next
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here
        source1_node = source1._front
        
        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)
            
            if current is None:
                # Value does not exist in this list
                new_node = _SL_Node(value, None)
                if self._rear is None:
                    # Target list empty, set it up
                    self._rear = new_node
                    self._front = new_node
                else:
                    # List non-empty, insert into proper spot
                    current = self._front
                    previous = None
                    
                    while current is not None and current._value < value:
                        previous = current
                        current = current._next
                    
                    new_node = _SL_Node(value, current)
                    if current is None:
                        # Reached end of list, add to end of list
                        self._rear._next = new_node
                        self._rear = new_node
                    else:
                        # Inserting somewhere in List, update proper references
                        previous._next = new_node
                self._count += 1
            source1_node = source1_node._next
            
        source2_node = source2._front
        
        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)
            
            if current is None:
                # Value does not exist in this list
                new_node = _SL_Node(value, None)
                if self._rear is None:
                    # Target list empty, set it up
                    self._rear = new_node
                    self._front = new_node
                else:
                    # List non-empty, insert into proper spot
                    current = self._front
                    previous = None
                    
                    while current is not None and current._value < value:
                        previous = current
                        current = current._next
                        
                    new_node = _SL_Node(value, current)
                    if current is None:
                        # Reached end of list, add to end of list
                        self._rear._next = new_node
                        self._rear = new_node
                    else:
                        # Inserting somwhere in List, update proper references
                        previous._next = new_node
                self._count += 1
            source2_node = source2_node._next
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
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """

        # your code here

        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (iterative version)
        Use: b = l.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """

        # your code here
        # Must be same size
        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            other_node = other._front
            
            while source_node is not None and source_node._value == other_node._value:
                source_node = source_node._next
                other_node = other_node._next
                
            identical = source_node is None
        return identical

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

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
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return

    def _linear_search_r(self, key):
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
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        # your code here

        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        # your code here

        return

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """

        # your code here

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

        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """

        # your code here

        return

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the current Sorted_List and rs
            are interlaced into new_list - current Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

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
            source1 - an linked list (List)
            source2 - an linked list (List)
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
