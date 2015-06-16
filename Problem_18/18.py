#Problem 18: Maximum path sum I
#Michael Ge, June 13, 2015

'''
Maximum path sum I
Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

#Variables
HEIGHT = 15
NUM_EL = (HEIGHT) * (HEIGHT + 1) / 2

#Node: contains a value and children nodes
class Node:
    def __init__(self, value, childL, childR):
        self.v = value
        self.cL = childL
        self.cR = childR

    def get_childL(self):
        return self.cL

    def get_childR(self):
        return self.cR

    def get_value(self):
        return self.v

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
    nodes.append(Node(x, None, None))
f.close()

#Triangle Graph Generation
inc = 0
for row in range(HEIGHT):
    for _ in range(1, row+1):
        nodes[inc].set_childL(nodes[inc+row])
        nodes[inc].set_childR(nodes[inc+row+1])
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
