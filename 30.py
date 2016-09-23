import sys

def fun(pos,money_list):
    if money_list==[]:
        return 0
    else:
        current_pos=money_list[0]
        tmp_list=money_list[1:]
        if pos==current_pos:
            return 1+fun(current_pos,tmp_list)
        elif pos+1==current_pos:
            return 1+fun(current_pos,tmp_list)
        elif pos-1==current_pos:
            return 1+fun(current_pos,tmp_list)
        else:
            if pos-1>=0:
                res1=fun(pos-1,tmp_list)
            else:
                res1=0
            if pos+1<=10:
                res2=fun(pos+1,tmp_list)
            else:
                res2=0
            res3=fun(pos,tmp_list)
            return max([res1,res2,res3])
            

if __name__=='__main__':
    a_line=map(int,sys.stdin.readline().strip().split())
    print a_line

    print fun(5,a_line)
