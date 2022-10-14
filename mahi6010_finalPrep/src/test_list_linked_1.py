"""
-------------------------------------------------------
Simple List testing - Exam
-------------------------------------------------------

-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from list_linked_1 import List

# Constants
SEP = '-' * 60
# These VALUES match the sample BST diagram on the exam web page:
# https://bohr.wlu.ca/cp164/exam
VALUES = [11, 7, 6, 9, 8, 15, 12, 18, 21]

print("List_linked Testing")
print()
print(SEP)
print("Test split_th")
source = List()
for value in VALUES:
    source.append(value)
print("Values in source (front to rear):")

for v in source:
    print(v, end=", ")
print()
target1, target2 = source.split_th()
print("After split")
print("Values in source (front to rear):")

for v in source:
    print(v, end=", ")
print()
print("Values in target1 (front to rear):")

for v in target1:
    print(v, end=", ")
print()
print("Values in target2 (front to rear):")

for v in target2:
    print(v, end=", ")
print()

print()
print(SEP)
print("Test shuffle")
source = List()
for value in VALUES:
    source.append(value)
print("Values in source (front to rear):")

for v in source:
    print(v, end=", ")
print()
target = source.shuffle()
print("After shuffle")
print("Values in source (front to rear):")

for v in source:
    print(v, end=", ")
print()
print("Values in target (front to rear):")

for v in target:
    print(v, end=", ")
print()
print(SEP)
