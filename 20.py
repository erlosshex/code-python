# needing more improvement

import sys

def calculate_time(b_list,c):
    result=0
    for i in xrange(len(b_list)):
        result=result+b_list[i]*c[i]
    return result

def deal_with(a_element,b):
    b.sort(reverse=True)

    if a_element==0:
        return []
    elif a_element<0 or len(b)==0:
        return None
    else:
        res1=deal_with(a_element,b[1:])#no
        res2=deal_with(a_element-b[0],b)#yes

        if res1==None:
            res1=[]
        elif res1==[]:
            res1=[]
        else:
            res1=res1

        if res2==[]:
            res2=[[b[0]]]
        elif res2==None:
            res2=[]
        else:
            for i in res2:
                i.append(b[0])
        res=[]
        for i in res1:
            res.append(i)
        for i in res2:
            res.append(i)

        return res

def filter_num(my_list,thread):
    return filter(lambda x: sum(x)==thread,my_list)
    



if __name__=='__main__':
    all_lines=map(lambda x: x.strip() ,sys.stdin.readlines())
    n=int(all_lines[0])
    a=map(int,all_lines[1:1+n])
    m=int(all_lines[1+n])
    b=[]
    c=[]
    for i in xrange(m):
        x,y=map(int,all_lines[2+n+i].split())
        b.append(x)
        c.append(y)
        
    result=[]

    for i in a:
        tmp_result=deal_with(i,b)
        tmp_result=filter_num(tmp_result,i)

        tmp_res=[]


        for item in tmp_result:
            tmp_count=[]

            for j in b:
                tmp_count.append(item.count(j))

            tmp_res.append(calculate_time(tmp_count,c))
        result.append(-1 if tmp_res==[] else min(tmp_res))


    min_result=filter(lambda x : x!=-1,result)

    if min_result==[]:
        print "it's not true!"
    else:
        print min(min_result)

        
    
