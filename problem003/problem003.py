#!/usr/bin/python3

'''
<p>The prime factors of 13195 are 5, 7, 13$ and $29.</p>
<p>What is the largest prime factor of the number 600851475143?</p>
'''

import math

target = 600851475143

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

result = 0
for v in primes():
	if v > math.sqrt(target):
		break
	if (target / v) % 1 == 0:
		result = v

print(result)
