""" A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

def find_pal(x,y):
    max_pal = 0
    for i in range(x,y+1):
        for j in range(i+1, y+1):
            k = i*j
            if k > max_pal and str(k) == str(k)[::-1]:
                max_pal = k
    print "The largest palindrome that is the product of two numbers between %d and %d is %d" % (x, y, max_pal)

find_pal(100,999)