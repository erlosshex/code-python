import sys

def fun(p,x_list):
    p_flag=[False]*p
    length=len(x_list)
    for i in xrange(length):
        xi=x_list[i]
        rem=xi%p
        if p_flag[rem]==True:
            return i+1
        else:
            p_flag[rem]=True

    return -1

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    p,n=map(int,all_lines[0].strip().split())
    x_list=map(int,all_lines[1:])

    print fun(p,x_list)
