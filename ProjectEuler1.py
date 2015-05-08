"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.  Find the sum of all the multiples of 3 or 5 below 1000.""" 
# create a function
def threefive(x):   
    
    #define variables
    sm = 0  
    y = 1
    
    #create a conditional
    while y < x:
        if y%5 == 0 or y%3 == 0:
            sm += y
        y += 1     
    
    #print the sum of all multiples of three and five less than x
    print(sm)

#call the function
threefive(1000)
