import sys

def calculate_score(num,num_list):
    return sum(map(lambda x: 3 if x>=num else 2,num_list))

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    a=map(int,all_lines[0].strip().split())
    b=map(int,all_lines[1].strip().split())

    a.sort()
    b.sort()

    result=[]
    for i in a:
        result.append(calculate_score(i,a)-calculate_score(i,b))
    print max(result)

    


