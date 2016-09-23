import sys

def check(l):
    tmp_l=[]
    result=[]
    length=len(l)
    i=1
    pre_num=l[0]
    tmp_l.append(pre_num)
    while i<length:
        if l[i]>=pre_num:
            result.append(tmp_l)
            tmp_l=[l[i]]
            pre_num=l[i]
            i=i+1
        else:
            
            tmp_l.append(l[i])
            pre_num=l[i]
            i=i+1
    result.append(tmp_l)
    return result

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    n=int(all_lines[0])
    read_list=[]

    for i in xrange(n):
        i=i*2+1
        first_line=map(int,all_lines[i].strip().split())
        second_line=map(int,all_lines[i+1].strip().split())


        tmp_list=[]
        for i in first_line:
            tmp_list.append(i)
        for i in second_line:
            tmp_list.append(i)


        read_list.append(tmp_list)

    for i in read_list:
        my_l=check(i[1:])
        my_l_num=map(lambda x:len(x)+1,my_l)
        my_l_num[0]=my_l_num[0]-1

        print max(my_l_num)
