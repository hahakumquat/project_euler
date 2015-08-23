
#Problem 15
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

