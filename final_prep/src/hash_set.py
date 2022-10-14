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


class Hash_Set():
    def _find_slot(self, key):
        hashkey = hash(key) % self._lots
        slot = self._table[hashkey]

    def _rehash(self):
        temp_table = self._table
        self._slots = self._slots * 2 + 1
        self._table = []
        for _ in range(self._slots):
            self._table.append([])
        while len(temp_table) > 0:
            old_slot = temp_table.pop(0)
            while not old_slot.is_empty():
                value = old_slot.remove_front()
                slot = self._find_slot(value)
                slot.insert(0, value)
        return

    def insert(self, value):
        LOAD_FACTOR = 20  # any constant
        slot = self._find_slot(value)
        if value in slot:
            inserted = False
        else:
            inserted = True
            slot.insert(0, value)
            self._count += 1
            if self._count > (LOAD_FACTOR * self._slots):
                self._rehash()
        return inserted

    def remove(self, key):
        slot = self._find_slot(key)
        value = slot.remove(key)
        if value is not None:
            self._count -= 1
        return value
