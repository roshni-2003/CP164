"""
------------------------------------------------------------------------
BST Implementations
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-20
------------------------------------------------------------------------
"""
from BST_linked import BST

print("Testing BST#is_balanced")

print("\n\nEmpty tree")
bst = BST()
print("Contents: {}".format([val for val in bst]))
balanced = bst.is_balanced()
print("Balanced? {}".format(balanced))
print("Expected: {}".format(True))

print("\n\nNon-empty tree not balanced")
bst = BST()
for val in [11,22,9,33,44,25]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
balanced = bst.is_balanced()
print("Balanced? {}".format(balanced))
print("Expected: {}".format(False))

print("\n\nNon-empty tree balanced")
bst = BST()
for val in [7,11,9,15,5,6,4]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
balanced = bst.is_balanced()
print("Balanced? {}".format(balanced))
print("Expected: {}".format(True))

print("\n\nTesting BST#is_valid")

print("\n\nEmpty bst")
bst = BST()
print("Contents: {}".format([val for val in bst]))
valid = bst.is_valid()
print("Valid? {}".format(valid))
print("Expected: {}".format(True))

print("\n\nNon-empty bst valid")
bst = BST()
for val in [11,8,15,6,7,0,18]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
valid = bst.is_valid()
print("Valid? {}".format(valid))
print("Expected: {}".format(True))

print("\n\nTesting BST#is_identical")

print("\n\nEmpty bsts")
bst = BST()
other = BST()
print("First contents: {}".format([val for val in bst]))
print("Other contents: {}".format([val for val in other]))
identical = bst.is_identical(other)
print("Identical? {}".format(identical))
print("Expected: {}".format(True))

print("\n\nFirst BST empty, other non-empty")
bst = BST()
other = BST()
for val in [7,3,9,1,4]:
    other.insert(val)
print("First contents: {}".format([val for val in bst]))
print("Other contents: {}".format([val for val in other]))
identical = bst.is_identical(other)
print("Identical? {}".format(identical))
print("Expected: {}".format(False))

print("\n\nFirst BST non-empty, other empty")
bst = BST()
other = BST()
for val in [7,3,9,1,4]:
    bst.insert(val)
print("First contents: {}".format([val for val in bst]))
print("Other contents: {}".format([val for val in other]))
identical = bst.is_identical(other)
print("Identical? {}".format(identical))
print("Expected: {}".format(False))

print("\n\nBoth non-empty, identical")
bst = BST()
other = BST()
for val in [7,3,9,1,4]:
    bst.insert(val)
    other.insert(val)
print("First contents: {}".format([val for val in bst]))
print("Other contents: {}".format([val for val in other]))
identical = bst.is_identical(other)
print("Identical? {}".format(identical))
print("Expected: {}".format(True))

print("\n\nTesting BST#min")

print("\n\nEmpty bst")
bst = BST()
print("Contents: {}".format([val for val in bst]))
try:
    min_value = bst.min()
except AssertionError:
    print("Cannot find min of empty bst, assertion thrown correctly.")

print("\n\nNon-empty bst")
bst = BST()
for val in [7,3,5,2,4,9]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
min_value = bst.min()
print("Returned min value: {}".format(min_value))
print("Expected: {}".format(2))

print("\n\nTesting BST#leaf_count")

print("\n\nEmpty bst")
bst = BST()
print("Contents: {}".format([val for val in bst]))
count = bst.leaf_count()
print("Leaf count: {}".format(count))
print("Expected: {}".format(0))

print("\n\nNon-empty bst, 1 leaf")
bst = BST()
for val in [7]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
count = bst.leaf_count()
print("Leaf count: {}".format(count))
print("Expected: {}".format(1))

print("\n\nNon-empty bst, more than 1 leaf")
bst = BST()
for val in [7,4,5,3,9,10,]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
count = bst.leaf_count()
print("Leaf count: {}".format(count))
print("Expected: {}".format(3))

print("\n\nNon-empty bst, more than 1 leaf")
bst = BST()
for val in [3,1,5,0,2,4,6]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
count = bst.leaf_count()
print("Leaf count: {}".format(count))
print("Expected: {}".format(4))

print("\n\nTesting BST#one_child_count")

print("\n\nEmpty BST")
bst = BST()
print("Contents: {}".format([val for val in bst]))
count = bst.one_child_count()
print("Num nodes w/ one child: {}".format(count))
print("Expected: {}".format(0))

print("\n\nNon-empty BST")
bst = BST()
for val in [7,15,4,5,3,1,18,16]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
count = bst.one_child_count()
print("Num nodes w/ one child: {}".format(count))
print("Expected: {}".format(3))

print("\n\nTesting BST#two_child_count")

print("\n\nEmpty BST")
bst = BST()
print("Contents: {}".format([val for val in bst]))
count = bst.two_child_count()
print("Num nodes w/ one child: {}".format(count))
print("Expected: {}".format(0))

print("\n\nNon-empty BST")
bst = BST()
for val in [7,15,4,5,3,1,18,16]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
count = bst.two_child_count()
print("Num nodes w/ one child: {}".format(count))
print("Expected: {}".format(2))

print("\n\nTesting BST#inorder")

print("\n\nEmpty bst")
bst = BST()
print("Contents: {}".format([val for val in bst]))
inorder = bst.inorder()
print("Inorder: {}".format(inorder))

print("\n\nNon-empty bst")
bst = BST()
for val in [7,15,4,6,5,2,3,1,18,14]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
inorder = bst.inorder()
print("Inorder: {}".format(inorder))

print("\n\nTesting BST#preorder")

print("\n\nEmpty bst")
bst = BST()
print("Contents: {}".format([val for val in bst]))
pre = bst.preorder()
print("Preorder: {}".format(pre))

print("\n\nNon-empty bst")
bst = BST()
for val in [7,15,4,6,5,2,3,1,18,14]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
pre = bst.preorder()
print("Preorder: {}".format(pre))

print("\n\nTesting BST#postorder")

print("\n\nEmpty bst")
bst = BST()
print("Contents: {}".format([val for val in bst]))
post = bst.postorder()
print("Postorder: {}".format(post))

print("\n\nNon-empty bst")
bst = BST()
for val in [7,15,4,6,5,2,3,1,18,14]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
post = bst.postorder()
print("Postorder: {}".format(post))

print("\n\nTesting BST#levelorder")

print("\n\nEmpty bst")
bst = BST()
print("Contents: {}".format([val for val in bst]))
level = bst.levelorder()
print("Levelorder: {}".format(level))

print("\n\nNon-empty bst")
bst = BST()
for val in [7,15,4,6,5,2,3,1,18,14]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
level = bst.levelorder()
print("Levelorder: {}".format(level))

print("\n\nTesting BST#remove")

print("\n\nEmpty bst")
bst = BST()
print("Contents: {}".format([val for val in bst]))
key = 4
print("Key: {}".format(4))
val = bst.remove(key)
print("Removed: {}".format(val))

print("\n\nNon-empty bst, key exists")
bst = BST()
for val in [7,3,4,2,15,18,11]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
key = 4
print("Key: {}".format(4))
val = bst.remove(key)
print("Removed: {}".format(val))

print("\n\nNon-empty bst, key does not exist")
bst = BST()
for val in [7,3,4,2,15,18,11]:
    bst.insert(val)
print("Contents: {}".format([val for val in bst]))
key = 20
print("Key: {}".format(4))
val = bst.remove(key)
print("Removed: {}".format(val))