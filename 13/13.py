#Problem 13
with open('test.txt') as f:
    l = f.readlines()
s = 0
for x in l:
    s = int(x) + s
print s

from num2words import num2words

sum = 0
for x in range(1,1001):
    x0 = num2words(x)
    x1 = x0.replace(" ", "")
    x2 = x1.replace("-", "")
    x3 = x2.replace(",", "")
    sum += len(x3)
print sum
