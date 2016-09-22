import sys
import math as m

def is_prime(num):
    middle=int(m.sqrt(num))
    for i in xrange(2,middle+1):
        if num%i==0:
            return False
    return True

if __name__=='__main__':
    number=input()
    #middle=int(m.sqrt(number))
    result=[]

    i=2

    while number!=1:
        if is_prime(i)==True:
            if number%i==0:
                result.append(i)
                number=number/i
                i=2
            else:
                i=i+1
        else:
            i=i+1
    #print '==='
    #print result
    #print '---'

    result.sort()

    result=map(str,result)
    result='*'.join(result)

    print result
        

    

    

    
