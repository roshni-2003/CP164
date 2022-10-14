"""
-------------------------------------------------------
Array-based list version of the Hash Set ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 A
__updated__ = "2019-02-18"
-------------------------------------------------------
"""
# Imports
# Use any appropriate data structure here.
from Sorted_List_array import Sorted_List
# Define the new_slot slot creation function.
new_slot = Sorted_List

# Constants
SEP = '-' * 40

class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, slots):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size slots.
        Use: hs = Hash_Set(slots)
        -------------------------------------------------------
        Parameter:
            slots - number of initial slots in Hash Set (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._slots = slots
        self._table = []
        self._count = 0

        # Define the empty slots.
        for _ in range(self._slots):
            self._table.append(new_slot())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """

        # your code here
        
        # Calculate the data's hash
        hash_value = hash(key)
        # Get the slot the data belongs in
        slot = hash_value % self._slots
        return self._table[slot]

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        slot = self._find_slot(key)
        return key in slot
        
    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        
        # Should we rehash?
        avg = self._count // self._slots
        should_rehash = avg >= self._LOAD_FACTOR
        #print(should_rehash)
        if should_rehash:
            #print("Rehash")
            #print("Count: {}\tSlots: {}\tAvg: {}".format(self._count, self._slots, avg))
            self._rehash()
        
        # Find the slot that the value belongs in
        slot = self._find_slot(value)
        
        # Don't add duplicates
        if value in slot:
            inserted = False
        else:
            # Value does not exist in the HS, insert into appropriate slot
            slot.insert(value)
            inserted = True
            self._count += 1
        
        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        # your code here

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        # your code here
        
        # Old code, updated 2019-03-20
        """
        # Find the slot the key is in
        slot = self._find_slot(key)
        value = None
        # Loop over the data in the slot
        for i in range(len(slot)):
            # Grab the current data to be processed
            data = slot[i]
            # Is the data the key we are looking for?
            if key == data:
                value = data
                # Remove the data from the slot. Duplicates not allowed 
                # so only one value will be removed
                slot.remove(data)
        """
        hash_value = hash(key)
        slot = hash_value % self._slots
        value = self._table[slot].remove(key)
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here
        CHANGE_FACTOR = 2 * self._slots + 1
        # Double the amount of slots in the Hash Set
        # Add the new slots to the table
        num_slots_to_add = CHANGE_FACTOR - self._slots
        for _ in range(num_slots_to_add):
            self._table.append(new_slot())
        # Update num slots to reflect slots just added
        self._slots = CHANGE_FACTOR
        # Loop over every slot
        for slot in self._table:
            # Loop over the data in the slot
            for data in slot:
                # Find new slot to put the data into
                slot_new = self._find_slot(data)
                # Not adding duplicates
                if data not in slot_new:
                    slot_new.insert(data)
        return

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two hash sets are identical.
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
             target - another hash set (Hash_Set)
        Returns:
            identical - True if this hash set contains the same values 
                as other in the same order, otherwise returns False.
        -------------------------------------------------------
        """

        # your code here

    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here
        print("{} slots".format(self._slots))
        
        for slot_num in range(self._slots):
            slot = self._table[slot_num]
            print(SEP)
            print("Slot {}".format(slot_num))
            for data in slot:
                print(data)
            print(SEP)
        
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item
