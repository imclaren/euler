#!/usr/bin/python3

# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a <> b, then a and b are an
# amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

from functools import reduce

def appendEs2Sequences(sequences,es):
    # See http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
    result=[]
    if not sequences:
        for e in es:
            result.append([e])
    else:
        for e in es:
            result+=[seq+[e] for seq in sequences]
    return result

def cartesianproduct(lists):
    """
    given a list of lists,
    returns all the possible combinations taking one element from each list
    The list does not have to be of equal length
    """
    # See http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
    return reduce(appendEs2Sequences,lists,[])

def get_prime_factors2(n):
    '''lists prime factors, from greatest to smallest (as a list)'''  
    # See http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
    from math import sqrt
    i = 2
    while i<=sqrt(n):
        if n%i==0:
            l = get_prime_factors2(n/i)
            l.append(i)
            return l
        i+=1
    return [n]      # n is prime

def factorGenerator(n):
    # See http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
    p = get_prime_factors2(n)
    factors={}
    for p1 in p:
        try:
            factors[p1]+=1
        except KeyError:
            factors[p1]=1
    return factors

def divisors(n):
    # See http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
    factors = factorGenerator(n)
    divisors=[]
    listexponents=[[k**x for x in range(0,factors[k]+1)] for k in list(factors.keys())]
    listfactors=cartesianproduct(listexponents)
    for f in listfactors:
        divisors.append(reduce(lambda x, y: x*y, f, 1))
    divisors.sort()
    return divisors

result = 0
l = []
for x in range(1,10000):
    a = sum(divisors(x)[:-1])
    if x != a: 
        l.append((x,a))
while l:
    ei = l.pop()
    for eo in l:
        if eo[0] == ei[1] and eo[1] == ei[0]: 
            result+=eo[0]+eo[1]
print(result)
