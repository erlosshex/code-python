import sys

def fun(a_list):
    then_list=a_list[:]
    n=len(a_list)

    for i in xrange(n):
        then_list[i]=a_list[(i+1)%n]+a_list[(i-1)%n]
    return then_list

def init_list(n):
    a_list=[0]*n
    a_list[0]=1
    return a_list

if __name__=='__main__':
    n,m=map(int,sys.stdin.readline().strip().split())

    a_list=init_list(n)
    for i in xrange(m):
        a_list=fun(a_list)

    print a_list[0]
