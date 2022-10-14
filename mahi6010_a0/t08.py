"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-01-10"
-------------------------------------------------------
"""
from functions import matrix_stats

mat = [[1, 6, 0, 2], [4, 0, 5, 9]]

small, large, total, average = matrix_stats(mat)

print("small: ", small, "\nlarge: ", large,
      "\ntotal: ", total, "\naverage: ", average)
