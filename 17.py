import sys

def is_huiwen(str_list):
    tmp_list=str_list[:]
    tmp_list.reverse()

    return sum(map(lambda x,y: 0 if x==y else 1,tmp_list,str_list))==0

if __name__=='__main__':
    a_line=list(sys.stdin.readline().strip())
    str_set=set(a_line)

    flag=False
    flag_loop=False

    for i in str_set:
        if flag_loop==True:
            break
        for j in xrange(len(a_line)+1):
            tmp_line=a_line[:]
            tmp_line.insert(j,i)
            if is_huiwen(tmp_line):
                flag=True
                flag_loop=True
                print 'YES'
                break

    if flag==False:
        print 'NO'

                
