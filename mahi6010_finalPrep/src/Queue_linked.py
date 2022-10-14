"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 A
__updated__ = "2018-10-31"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """

        # Your code here

        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """

        # Your code here

        return 

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """

        # Your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """

        # Your code here
        new_node = _Queue_Node(value, None)
        if self._rear is None:
            # First element
            self._rear = new_node
            self._front = new_node
        else:
            # Just adding to the rear of the Queue
            self._rear._next = new_node
            self._rear = new_node
        self._count += 1
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"


        # Your code here
        value = deepcopy(self._front._value)
        self._front = self._front._next
        self._count -= 1
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"


        # Your code here
        value = deepcopy(self._front._value)
        return value

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Equivalent of:
        self.insert(source.remove()), but moves nodes not data.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"


        # Your code here
        new_node = _Queue_Node(source._front._value, None)
        if self._rear is None:
            self._rear = new_node
            self._front = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
            
        self._count += 1
        if source._count == 1:
            source._front = None
            source._rear = None
            source._count = 0
        else:
            source._front = source._front._next
            source._count -= 1
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"


        # Your code here
        source_node = source._front
        while source_node is not None:
            self._rear._next = source_node
            self._rear = source_node
            source_node = source_node._next
            source._count -= 1
            self._count += 1
            source._front = source._front._next
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """

        # Your code here
        
        # Used if one of the sources are empty
        main_source = None
        
        if source1._front is None and source2._front is not None:
            # Source1 empty, using source2
            new_node = _Queue_Node(source2._front._value, None)
            if self._rear is None:
                self._rear = new_node
                self._front = new_node
            else:
                self._rear._next = new_node
                self._rear = new_node
            self._count += 1
            source2._front = source2._front._next
            source2._count -= 1
            main_source = source2
        elif source2._front is None and source1._front is not None:
            # Source2 empty, using source1
            new_node = _Queue_Node(source1._front._value, None)
            if self._rear is None:
                self._rear = new_node
                self._front = new_node
            else:
                self._rear._next = new_node
                self._rear = new_node
            self._count += 1
            source1._front = source1._front._next
            source1._count -= 1
            main_source = source1
        elif source1._front is not None and source2._front is not None:
            # Both have nodes, start interlacing
            new_node = _Queue_Node(source1._front._value, None)
            if self._rear is None:
                self._rear = new_node
                self._front = new_node
            else:
                self._rear._next = new_node
                self._rear = new_node
            self._count += 1
            source1._count -= 1
            source1._front = source1._front._next
            
            new_node = _Queue_Node(source2._front._value, None)
            # No need for a check if rear is None
            self._rear._next = new_node
            self._rear = new_node
            self._count += 1
            source2._count -= 1
            source2._front = source2._front._next
        
        # Both source1 and source2 have nodes
        if main_source is None:
            source1_node = source1._front
            source2_node = source2._front
            
            while source1_node is not None:
                self._rear._next = source1_node
                self._rear = source1_node
                self._count += 1
                source1_node = source1_node._next
                source1._front = source1._front._next
                source1._count -= 1
                if source2_node is not None:
                    self._rear._next = source2_node
                    self._rear = source2_node
                    self._count += 1
                    source2_node = source2_node._next
                    source2._front = source2._front._next
                    source2._count -= 1
        else:
            # One source is empty, so use other
            current = main_source._front
            while current is not None:
                self._rear._next = current
                self._rear = current
                self._count += 1
                current = current._next
                main_source._front = main_source._front._next
                main_source._count -= 1
                
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains remaining values from source (Queue)
        -------------------------------------------------------
        """

        # Your code here
        target1 = Queue()
        target2 = Queue()
        left = True
        
        while self._front is not None:
            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
        return target1, target2

    def is_identical(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Values of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """

        # Your code here
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            other = target._front
            
            while source_node is not None and source_node._value == other._value:
                source_node = source_node._next
                other = other._next
                
            identical = source_node is None
        return identical

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
