#!/usr/bin/python3

# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def get_slist(n):
    v = n
    count = 1
    while v != 1:
        if v%2: 
            v = (3*v)+1
        else: 
            v = v/2
        count += 1
    return count

limit = 999999
result = 0
chain_length = 0
for i in range(0, limit):
    v = get_slist(i+1)
    if v > chain_length:
        chain_length = v
        result = i+1

print(result)
