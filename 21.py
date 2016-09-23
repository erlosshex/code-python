import sys


def gcd(m,n):
    mm=max(m,n)
    nn=min(m,n)

    r=mm%nn
    if r==0:
        return nn
    else:
        return gcd(nn,r)

def fun(start,my_list):
    current=start
    for i in my_list:
        if i<=current:
            current=current+i
        else:
            current=current+gcd(current,i)
    return current

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    length=len(all_lines)/2

    read_result=[]

    for i in xrange(length):
        i=i*2
        first_line=map(int,all_lines[i].strip().split())
        second_line=map(int,all_lines[i+1].strip().split())
        first_line.extend(second_line)
        read_result.append(first_line)

    for i in read_result:
        print fun(i[1],i[2:])

        
