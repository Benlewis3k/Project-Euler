"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
#first we declare a function is_prime that checks if a number is prime.
def is_prime(x):
	if x % 2 == 0:
		return False
	i = 3
	while  i**2 < x:
		if x % i == 0:
			return False
		else:
			i += 2
	return True	

#next we declare a function that checks each odd number to see if it is prime.
#this process is repeated until we find the nth prime.

def nth_prime(x):
	n = 1
	p = 2
	i = 3
	while n < x:
		if is_prime(i):
			n += 1
			p = i
		i += 2
	print("Prime number %d is %d" % (x, p))

nth_prime(10001)