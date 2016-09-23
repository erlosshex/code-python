import sys

def check(l,g):
    return l in g

def check_out(l,g):
    return list(filter(lambda x: x[0]==l[1] and x[1]!=l[0],g))

def deal_with(l,g,km):

    if check(l,g)==False:
        return 0
    else:
        count=0
        for i in xrange(l[2]):
            km=km+1
            count=count+km+10
            pass
        tmp_g=check_out(l,g)
        tmp_res=[]
        for i in tmp_g:
            tmp_res.append(deal_with(i,g,km))

        if tmp_res==[]:
            return count
        else:
            return max(tmp_res)+count

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    n=int(all_lines[0])
    G=[]

    for i in xrange(1,n):
        a_line=all_lines[i]
        p,q,d=map(int,a_line.strip().split())
        G.append([p,q,d])

    tmp_G=map(lambda x:[x[1],x[0],x[2]],G)
    G.extend(tmp_G)

    result=[]

    for i in G:
        num=deal_with(i,G,0)
        result.append(num)

    print max(result)

