import sys

def calculate(num):
    c=[0,1,2]
    if num-1 in c:
        return c[num-1]
    else:
        return calculate(num-1)+calculate(num-2)

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    all_lines=map(int,all_lines)
    number=all_lines[0]
    stair_list=all_lines[1:]

    for i in stair_list:
        print calculate(i)


        

    

    

    
