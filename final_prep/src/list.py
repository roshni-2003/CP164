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


class List:
    def __init__(self):
        self._values = []

    def __getitem__(self, i):
        return deepcopy(self._values[i])

    def __len__(self):
        return len(self._values)

    def __setitem__(self, i, value):
        self._values[i] = deepcopy(value)

    def append(self, value):
        self._values += [deepcopy(value)]

    def peek(self, index):
        return deepcopy(self._values[index])

    def return_values(self):
        return deepcopy(self._values)


class Diary:
    def __init__(self):
        self.entries = List()

    def new_entry(self, val):
        self.entries.append(val)

    def view_entry(self, day):
        return self.entries.peek(day)

    def edit_entry(self, index, editedVal):
        self.entries[index] = editedVal

    def return_entries(self):
        return self.entries.return_values()


diary = Diary()

first_entries = ["hello", "i is in love", "exams are killing me"]

for i in first_entries:
    diary.new_entry(i)

print(f"Diary entries so far: {diary.return_entries()}")

print(f"Diary entry 0 is {diary.view_entry(0)}")
