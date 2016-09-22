import sys

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    n=int(all_lines[0])
    people_list=map(lambda x: map(int,x.split()),all_lines[1:])

    result=0
    people_number=0

    for x,y in people_list:
        people_number=people_number+y-x
        if people_number>result:
            result=people_number

    print result

