import sys

G='Gongfei'
Z='Zifei'
F='Fail'

def check(a_list):
    tmp_sum=sum(a_list)
    a,b,c,d=a_list

    if a>=60 and b>=60 and c>=90 and d>=90:
        if tmp_sum>=310:
            if tmp_sum>=350:
                print G
            else:
                print Z
        else:
            print F
    else:
        print F

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    num=int(all_lines[0])

    result_list=map(lambda x: map(int,x.split()),all_lines[1:])

    for i in result_list:
        check(i)

    

