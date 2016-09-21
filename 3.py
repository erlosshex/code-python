import sys

def is_right(origin_list):
    tmp_list=origin_list[:]
    tmp_list.sort(reverse=True)
    return sum(map(lambda x,y:abs(x-y),origin_list,tmp_list))==0

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    num=int(all_lines[0])
    num_list=map(int,all_lines[1].split())

    tmp_num_list=num_list[:]
    num_list.sort()

    index=[]
    for i in xrange(len(num_list)):
        if tmp_num_list[i]!=num_list[i]:
            index.append(i)

    if index[-1]-index[0]+1 == len(index):
        tmp_list=[]
        for i in index:
            tmp_list.append(tmp_num_list[i])
        if is_right(tmp_list)==True:
            sys.stdout.write('yes\n')
        else:
            sys.stdout.write('no\n')
    else:
        sys.stdout.write('no\n')


    

    
