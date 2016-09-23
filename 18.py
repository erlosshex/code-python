import sys

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    n,m=map(int,all_lines[0].strip().split())
    people_list=map(int,all_lines[1].strip().split())

    c=m
    current_c=0
    count_car=1
    i=0

    while i<n:
        current_c=current_c+people_list[i]
        if current_c<c:
            i=i+1
            continue
        elif current_c==c:
            i=i+1
            continue
        else:
            current_c=0
            count_car=count_car+1
            continue

    print count_car
        
    
