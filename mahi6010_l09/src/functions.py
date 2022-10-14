"""
------------------------------------------------------------------------
Lab 9 - functions module
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-17
------------------------------------------------------------------------
"""
from Movie import Movie
def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.    
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    # Set up table headers
    print("{}     {} {}".format("Hash", "Slot", "Key"))
    print("-"*8,end=' ')
    print("-"*4, end=' ')
    print("-"*20)
    
    # Calculate the hashes, slot, and display them with the key
    for val in values:
        hash_value = hash(val)
        slot = hash_value % slots
        key = Movie(val.title, val.year, None, None, None)
        print("{}\t  {}   {}".format(hash_value, slot, key))
    return