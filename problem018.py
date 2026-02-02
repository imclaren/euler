#!/usr/bin/python3

# By starting at the top of the triangle below and moving
# to adjacent numbers on the row below, the maximum total from
# top to bottom is 23.
#    3
#   7 5
#  2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom of the triangle below:
# NOTE: As there are only 16384 routes, it is possible to solve this
# problem by trying every route. However, Problem 67, is the same
# challenge with a triangle containing one-hundred rows; it cannot
# be solved by brute force, and requires a clever method! ;o)

# Solutions to problems 18 and 67 are identical 

f = open('problem018.txt', 'r')
t = []
for line in iter(f.readline, ''):
    t.append([int(row) for row in line.split()]) # This also removes \n
f.close()

result = 0
while len(t) > 1:
    lastline = t.pop()
    while len(lastline) > 1:
        lastnum = lastline.pop()
        t[-1][len(lastline)-1] += max(lastnum,lastline[-1])
    result = t[0][0]
print(result) 
