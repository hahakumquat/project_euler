'''
Problem 15
SIZE = 21
arr = [[0 for _ in range(SIZE+1)] for _ in range(SIZE+1)]
arr[SIZE][SIZE-1] = 1
for k in range(SIZE)[::-1]:
    for j in range(k+1):
        arr[k-j][k] = arr[k-j+1][k] + arr[k-j][k+1]
        arr[k][k-j] = arr[k][k-j+1] + arr[k+1][k-j]
for k in range(0, SIZE+1):
    print arr[k]

import math
x = int(math.pow(2,1000))
z = 0;
while x > 0:
    z += x%10
    x/=10
print z
'''

'''
Problem 13
with open('test.txt') as f:
    l = f.readlines()
s = 0
for x in l:
    s = int(x) + s
print s
'''
from num2words import num2words

sum = 0
for x in range(1,1001):
    x0 = num2words(x)
    x1 = x0.replace(" ", "")
    x2 = x1.replace("-", "")
    x3 = x2.replace(",", "")
    sum += len(x3)
print sum
