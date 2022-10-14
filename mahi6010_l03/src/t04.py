"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-05-26"
-------------------------------------------------------
"""

from utilities import array_to_queue
from utilities import queue_to_array


target = []

queue = [11, 22, 33, 44]

queue_to_array(queue, target)

print(target)
