import sys

length=20
width=2

def fun(r_list):
    count=0
    l=0
    i=0
    while(i<len(r_list)):
        l=l+2*r_list[i]
        if l<=length:
            count=count+1
        i=i+1
    count=count+1

    return count

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    first_line=int(all_lines[0])
    second_line=map(float,all_lines[1].strip().split())

    second_line.sort(reverse=True)

    print fun(second_line)
