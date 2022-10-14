"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-04-14"
-------------------------------------------------------
"""


def hash(str):
    value = 0
    for c in str:
        value = value + ord(c)
    return value


def cypher(string):
    scrambled = ""
    for c in string:
        scrambled = scrambled + str(ord(c)) + " "
    return scrambled[:-1]


def decypher(string):
    unscrambled = ""
    str_list = string.split()
    for i in str_list:
        unscrambled += chr(int(i))
    return unscrambled


text = "LCS wishes you the best on your finale"
print(f"Text to cypher: {text}")
print("----------------------------------------")
print()
print(f"Cyphered: {cypher(text)}")
cyph = cypher(text)
print()
print("----------------------------------------")
print()
print(f"Decyphered: {decypher(cyph)}")
