#!/usr/bin/python3

# n! means n*(n-1) x ... x 3 x 2 x 1
# Find the sum of the digits in the number 100!

def get_factorial(x):
    '''n! means n*(n-1) x ... x 3 x 2 x 1'''
    return (1 if x==0 else x*get_factorial(x-1))

result = sum([int(a) for a in str(get_factorial(100))])
print(result)
