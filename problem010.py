#!/usr/bin/python3

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

target = 2000000

result = 0
count = 0
for a in primes():
	if a >= target: 
		break
	else:
		count += 1
		result += a

print(result)