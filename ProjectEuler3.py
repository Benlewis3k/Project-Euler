"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

#define the fuction
def largest_factor(x):
    
    #define variables
    n = x
    i = 2
    
    #loop over n until we find the largest factor of x
    while i^2 < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    
    #declare the solution
    print "The largest factor of %d is %d" % (x, n)
    
#call the function
largest_factor(600851475143)