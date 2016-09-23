#need more improvement --- pai lie

import sys

def c(l,m):
    if m==0:
        return []
    else:
        res=[]
        for i in l:
            tmp_l=l[:]
            tmp_l.remove(i)
            tmp_res=c(tmp_l,m-1)
            if tmp_res==[]:
                res.append([i])
            else:
                for item in tmp_res:
                    item.append(i)
                tt=tmp_res
                for ttt in tt:
                    res.append(ttt)
        return res
        

if __name__=='__main__':
    a_line=sys.stdin.readline()
    n,a,b,x=map(int,a_line.strip().split())
    a_range=range(a,b+1)

    result_list=c(a_range,n)

    num=sum(map(lambda y: 1 if sum(y)==x else 0,result_list))/2

    number=len(result_list)/2

    out='%.4f'%(float(num)/number)

    print out    

