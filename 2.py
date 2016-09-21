import sys

if __name__=='__main__':
    a_line=sys.stdin.readline()
    num_list=a_line.split()

    num_list=map(int,num_list)
    
    min_num=num_list[0]
    max_num=num_list[1]
    bin_num=num_list[2]

    my_correct=0

    for i in xrange(min_num,max_num+1):
        tmp=bin(i)
        my_sum=sum(map(int,tmp[2:]))
        if my_sum==bin_num:
            my_correct=my_correct+1

    if my_correct==0:
        sys.stdout.write(str(-1)+'\n')
    else:
        sys.stdout.write(str(my_correct)+'\n')
