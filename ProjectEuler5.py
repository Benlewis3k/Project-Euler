""" 2520 is the smallest number that can be divided by 
each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20? """

def divis():
    a = 2520
    check_list = [11, 13, 15, 16, 17, 19]
    for i in xrange(2520, 1000000000, 2520):
        if all(i % j == 0 for j in check_list):
            print "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is %d" % i
            break
divis() 