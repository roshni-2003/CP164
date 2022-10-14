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


class Queue:
    def __init__(self):
        self._values = []

    def enqueue(self, data):
        self._values.append(data)

    def dequeue(self):
        if len(self._values) > 0:
            return deepcopy(self._values.pop(0))
        else:
            return "Nothing more to see"

    def peek(self):
        if len(self._values) > 0:
            return deepcopy(self._values[0])
        else:
            return "Nothing more to see"

    def return_values(self):
        return deepcopy(self._values)


class GroceryStoreCheckout:
    def __init__(self):
        self.items = Queue()

    def addItemToBelt(self, item):
        self.items.enqueue(item)

    def removeItemFromBelt(self):
        return self.items.dequeue()

    def viewItem(self):
        return self.items.peek()

    def viewBelt(self):
        return self.items.return_values()


items_on_belt = GroceryStoreCheckout()

items = ["Apple", "Banana", "Orange"]

for item in items:
    items_on_belt.addItemToBelt(item)

print(f"Items on belt: {items_on_belt.viewBelt()}")

print("\n")
input()

while items_on_belt.viewItem() != "Nothing more to see":
    items_on_belt.removeItemFromBelt()
'''
print("Scanning Items")
print("----------------")
print("Item 1 Scanned")
items_on_belt.removeItemFromBelt()
print(f"Items on belt: {items_on_belt.viewBelt()}")

print("\n")
input()

print("Scanning Items")
print("----------------")
print("Item 2 Scanned")
items_on_belt.removeItemFromBelt()
print(f"Items on belt: {items_on_belt.viewBelt()}")

print("\n")
input()

print("Scanning Items")
print("----------------")
print("Item 3 Scanned")
items_on_belt.removeItemFromBelt()
'''
print(f"Items on belt: {items_on_belt.viewBelt()}")
