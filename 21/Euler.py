#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

def sumDivisors(n):
    sum = 0
    for k in range(1, round(n/2) + 1):
        if n%k==0:
            sum+=k
    return sum

def search(s, t):
    for k in s:
        if k == t:
            return True
    return False

def amicable(nums):
    sum = 0
    s = set()
    for n in range(1, nums):
        dn = sumDivisors(n)
        if (n < dn):
            if (search(s, (n, dn))):
                sum += n
                sum += dn
                s.remove((n, dn))
            else:
                s.add((n, dn))
        else:
            if (search(s, (dn, n))):
                sum += dn
                sum += n
                s.remove((dn, n))
            else:
                s.add((dn, n))
    return sum

print(amicable(10000))
