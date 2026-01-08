#!/usr/bin/python3

'''
 <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is 9009 = 91 times 99$.</p>
 <p>Find the largest palindrome made from the product of two 3$-digit numbers.</p>
'''

def is_pal(n):
	l = list(str(n))
	if len(l) == 3:
		if l[0] == l[2]:
			return True
	if len(l) == 4:
		if l[0] == l[3] and l[1] == l[2]:
			return True
	if len(l) == 5:
		if l[0] == l[4] and l[1] == l[3]:
			return True
	if len(l) == 6:
		if l[0] == l[5] and l[1] == l[4] and l[2] == l[3]:
			return True
	return False

result = 0
for a in range(100, 1000):
	for b in range(100, 1000):
		v = a*b
		if is_pal(v) and v > result:
			result = v

print(result)
