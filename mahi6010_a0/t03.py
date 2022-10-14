"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-01-07"
-------------------------------------------------------
"""
from functions import file_analyze

fv = open("sentences.txt", "r")

u, l, d, w, r = file_analyze(fv)

print("Uppercase: ", u, "\nLowercase: ", l, "\nDigit: ",
      d, "\nWhitespace: ", w, "\nRemaining: ", r)

fv.close()
