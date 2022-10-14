"""
------------------------------------------------------------------------
Lab 9, Task 3 - Hash_Set#debug
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-18
------------------------------------------------------------------------
"""
from Hash_Set_array import Hash_Set
from Movie_utilities import read_movies

NUM_SLOTS = 7

print("\nTesting Hash_Set#debug()")

print("\n\nEmpty Hash_Set")
hs = Hash_Set(NUM_SLOTS)
hs.debug()

print('\n\nNon-empty Hash_Set')
for i in [1,2,3,4]:
    hs.insert(i)
hs.debug()

print("\n\nHash_Set with movies")
fh = open('movies.txt', 'r')
movies = read_movies(fh)

hs = Hash_Set(NUM_SLOTS)
for movie in movies:
    hs.insert(movie)

hs.debug()