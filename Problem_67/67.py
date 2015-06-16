#Problem 18: Maximum path sum I
#Michael Ge, June 13, 2015

'''
By starting at the top of the triangle below and moving to adjacent numbers
 on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a
triangle with one-hundred rows.
'''

#Variables
HEIGHT = 100
NUM_EL = (HEIGHT) * (HEIGHT + 1) / 2

#Node: contains a value, a parent node, and a child node
class Node:
    def __init__(self, value, parent, childL, childR):
        self.v = value
        self.p = parent
        self.cL = childL
        self.cR = childR

    def get_parent(self):
        return self.p

    def get_childL(self):
        return self.cL

    def get_childR(self):
        return self.cR

    def get_value(self):
        return self.v

    def set_parent(self, _p):
        self.p = _p

    def set_childL(self, _c):
        self.cL = _c

    def set_childR(self, _c):
        self.cR = _c

    def set_value(self, _v):
        self.v = _v

#Data Input
with open('test.txt') as f:
    nums = map(int, f.read().split())
nodes = []

for x in nums:
    nodes.append(Node(x, None, None, None))
f.close()

#Triangle Graph Generation
inc = 0
for row in range(HEIGHT):
    for _ in range(1, row+1):
        nodes[inc].set_childL(nodes[inc+row])
        nodes[inc].set_childR(nodes[inc+row+1])
        nodes[inc+row].set_parent(nodes[inc])
        nodes[inc+row+1].set_parent(nodes[inc])
        inc+=1

#Largest Sum Algorithm; Compares right to left up the tree
for node in nodes[::-1]:
    left = node.get_childL()
    right = node.get_childR()
    if left is not None and right is not None:
        node.set_value(node.get_value() +
                       max(left.get_value(), right.get_value()))
    elif left is not None:
        node.set_value(node.get_value() + left.get_value())
    elif right is not None:
        node.set_value(node.get_value() + right.get_value())

print nodes[0].get_value()
