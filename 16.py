import sys

def lift_way(n,m,t1,t2,t3,t4):
    return t2+t3+t2+t1*abs(n-m)+t1*(n-1)

def stair_way(n,t4):
    return t4*(n-1)

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    n,m=map(int,all_lines[0].strip().split())
    t1,t2,t3,t4=map(int,all_lines[1].strip().split())

    stair_num=stair_way(n,t4)
    lift_num=lift_way(n,m,t1,t2,t3,t4)

    print min(stair_num,lift_num)
