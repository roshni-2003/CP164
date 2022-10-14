"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-06-03"
-------------------------------------------------------
"""
from Queue_circular import Queue

q = Queue(3)

print(len(q))

print(q.is_empty())

q.insert(100)

print(len(q))

value = q.peek()

print(value)

removed = q.remove()

print(removed)

q.insert(100)
q.insert(200)
q.insert(300)
print(q.is_full())
