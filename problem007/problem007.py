#!/usr/bin/python3

'''
<p>By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6$th prime is 13$.</p>
<p>What is the 10,001st prime number?</p>
'''

import math

def is_prime(v):
	a = 2
	while True:
		if a > math.sqrt(v):
			break
		if v % a == 0: 
			return False
		a += 1
	return True

def primes():
	yield(2)
	a = 1
	while True:
		a += 2
		if is_prime(a):
			yield(a)

i = 0
for v in primes():
	i += 1
	if i == 10001:
		print(v)
		break