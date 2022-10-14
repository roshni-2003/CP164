"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-04-13"
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:
    def __init__(self):
        self._values = []

    def push(self, val):
        self._values.append(val)

    def pop(self):
        return self._values.pop()

    def peek(self):
        return deepcopy(self._values[-1])


class Restaurant:
    def __init__(self):  # initializing stack into self.plates
        self.plates = Stack()
        self.washedPlates = Stack()  # unrelated to above stack

    def addPlate(self, plate):
        self.plates.push(plate)

    def removePlate(self):
        return self.plates.pop()  # removes first object and tells what it is

    def checkPlate(self):
        return self.plates.peek()  # only tells you what the first object is


rest = Restaurant()

# LOFI
rest.addPlate("plate 1")
rest.addPlate("plate 2")
rest.addPlate("plate 3")
rest.addPlate("plate 4")
rest.addPlate("plate 5")

rest.removePlate()  # removes and returns plate 5

print(f"Plate on top of the pile: {rest.checkPlate()}")  # will return plate 4
