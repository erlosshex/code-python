# needing more improvement

import sys

def fun(V,my_list):
    tmp_list=my_list[:]
    tmp_list.sort()
    length=len(tmp_list)

    count=0
    i=0
    while V-tmp_list[i]>=0 and i<length:
        i=i+1
        V=V-tmp_list[i]
        count=count+1

    return count

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

    for item in read_result:
        print fun(item[1],item[2:])

        
