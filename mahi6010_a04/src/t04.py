"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-06-04"
-------------------------------------------------------
"""
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in l:
    pq.insert(i)

list1, list2 = pq_split_key(pq, 5)
list3 = []

print("List 1: ")
for i in list1:
    print(i)
    list3.append(i)
print("\nList 2: ")
for i in list2:
    print(i)
    list3.append(i)

print("\nList 3: ")
for i in list3:
    print(i)
