'''
Problem 22
Michael Ge, June 16, 2015

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714.
What is the total of all the name scores in the file?
'''
import string
import time
#Variables
t = time.time()
#File Input
with open("names.txt") as f:
    names = f.read().split(",")
f.close()

#Sorting
a = [[] for _ in range(26)]
for n in names:
    a[ord(n[1])-65].append(n)
map(list.sort, a)

#Summing
tot = 0
ctr = 0
for letter in a:
    for name in letter:
        ctr += 1
        tot += ctr * (sum(map(ord, name[1:len(name)-1])) - 64*(len(name) - 2))

t2 = time.time()
print tot
print t2 -t
