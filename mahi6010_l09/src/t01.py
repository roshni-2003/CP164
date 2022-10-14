"""
------------------------------------------------------------------------
Lab 9, Task 1 - hash_table
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-17
------------------------------------------------------------------------
"""
from functions import hash_table
from Movie_utilities import read_movies

fh = open('movies.txt', 'r')
movies = read_movies(fh)
print("Hashes")
hash_table(7, movies)
