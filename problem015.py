#!/usr/bin/python3

# Starting in the top left corner of a 2x2 grid, there are 6 routes
# (without backtracking) to the bottom right corner.
# How many routes are there through a 20x20 grid?

# 15, 20, 34
def get_factorial(x):
    '''n! means n*(n-1) x ... x 3 x 2 x 1'''
    return (1 if x==0 else x * get_factorial(x-1))


# (rows+columns)! / rows! * columns!
rows = 20
columns = 20
a = get_factorial(rows+columns)
b = get_factorial(rows)
c = get_factorial(columns)    
result = a/(b*c)

print(result)
