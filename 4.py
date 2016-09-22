import sys

def find_max_between(position_list):
    tmp_list=position[:]
    tmp_list.sort()
    x,y,max_between=0,0,0

    for i in xrange(len(tmp_list)-1):
        tmp_between=abs(tmp_list[i]-tmp_list[i+1])
        if tmp_between>max_between:
            x,y,max_between=tmp_list[i],tmp_list[i+1],tmp_between

    return x,y,max_between

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    number,length=map(int,all_lines[0].split())
    position=map(int,all_lines[1].split())

    tmp_position=list(set(position)|set([0])|set([length]))

    x,y,between=find_max_between(tmp_position)

    if x==0:
        if x in position:
            sys.stdout.write('%.2f\n'%(between/2.0))
        else:
            sys.stdout.write('%.2f\n'%(between))
    elif y==length:
        if y in position:
            sys.stdout.write('%.2f\n'%(between/2.0))
        else:
            sys.stdout.write('%.2f\n'%(between))
    else:
        sys.stdout.write('%.2f\n'%(between/2.0))

    

    

    
