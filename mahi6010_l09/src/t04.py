"""
------------------------------------------------------------------------
Lab 9, Task 4 - Hash_Set#rehash()
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-18
------------------------------------------------------------------------
"""
from Hash_Set_array import Hash_Set
from Movie_utilities import read_movies
from random import randint

hs = Hash_Set(1)
fh = open('movies.txt', 'r')
movies = read_movies(fh)

"""
for i in range(100):
    for movie in movies:
        hs.insert(movie)
"""
for i in range(50):
    value = randint(0, 1000)
    hs.insert(value)
print("Slots: {}\tCount: {}\tAvg: {}\tLoad Factor: {}".format(hs._slots, hs._count, hs._count // hs._slots, hs._LOAD_FACTOR))
hs.debug()