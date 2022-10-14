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
from functions import queue_combine
from Queue_array import Queue

source1 = Queue()
source1.insert(4)
source1.insert(1)
source1.insert(7)
source1.insert(3)
source1.insert(9)

source2 = Queue()

source2.insert(2)
source2.insert(4)
source2.insert(5)
source2.insert(1)
source2.insert(0)
source2.insert(9)

print([x for x in source1])
print([x for x in source2])

target = queue_combine(source1, source2)

print([x for x in target])
