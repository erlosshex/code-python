# needing more improvement

import sys

def is_overlap(l1,l2):
    len1=len(l1)
    len2=len(l2)
    x1,y1=l1
    x2,y2=l2
    if len1>len2:
        if (x2>=x1 and x2<=y1) or (y2>=x1 and y2<=y1):
            return True
        else:
            return False
        
    else:
        if (x1>=x2 and x1<=y1) or (y1>=x2 and y1<=y2):
            return True
        else:
            return False

def fun(l1,l2):
    for i in l1:
        for j in l2:
            if is_overlap(i,j):
                return True

    return False

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    p,q,l,r=map(int,all_lines[0].strip().split())

    m=[]
    for i in xrange(1,p+1):
        m.append(map(int,all_lines[i].strip().split()))
    h=[]
    for i in xrange(1+p,1+p+q):
        h.append(map(int,all_lines[i].strip().split()))
        
    print sum(map(lambda x: 1 if fun(m,map(lambda y: [y[0]+x,y[1]+x],h)) else 0 ,xrange(1,r+1)))
