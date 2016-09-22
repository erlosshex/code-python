import sys

c_list='abcdefghijkl'

def fun(n):
    if n==0:
        return 1
    else:
        return n*fun(n-1)

def check(c,tmp_list):
    return sum(map(lambda x: 1 if x<c else 0, tmp_list))

def calculate(a_list):
    n=len(a_list)
    result=0
    tmp_c_list=list(c_list[:])
    for i in a_list:
        tmp_c_list.remove(i)
        n=n-1
        tmp=check(i,tmp_c_list)
        if tmp==0:
            continue
        else:
            result=result+tmp*fun(n)
    return result

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    num=int(all_lines[0])

    item_list=map(lambda x:x.strip(),all_lines[1:])

    for i in item_list:
        print calculate(i)+1
    

    

