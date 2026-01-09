#!/usr/bin/python3

'''
<p>2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.</p>
<p>
	What is the smallest positive number that is 
	<strong class="tooltip">
		evenly divisible
		<span class="tooltiptext">divisible with no remainder</span>
	</strong>
		by all of the numbers from 1 to 20?
</p>
'''

result = 20
done = False
while not done:
	done = True
	result += 20
	for a in range(1, 20):
		if result % a != 0:
			done = False
			break
	
print(result)