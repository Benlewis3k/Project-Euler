""" 

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def sq_diff(x):
	i = 1
	smsq = 0
	sqsm = 0
	sm = 0 
	while i < x+1:
		smsq += i**2
		sm += i
		i += 1
	sqsm = sm**2
	print("The sum of the first %d squares is %d" % (x, smsq))
	print("The square of the sum of the first %d integers is %d" % (x, sqsm))
	print("The difference between the sum of the squares and square of the sums is %d" % (sqsm - smsq))
sq_diff(100)
