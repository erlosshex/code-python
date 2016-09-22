import sys

def judge(x):
    if x.isalpha() or x.isdigit():
        return 1
    else:
        return 0

def check(x,y):
    if x==y:
        return 1
    else:
        return 0

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    first_line=all_lines[0][:-1]
    second_line=all_lines[1][:-1]

    first_line=map(judge,first_line)
    second_line=map(int,second_line)

    result=sum(map(check,first_line,second_line))

    print '%.2f%%'%(float(result*100)/len(first_line))

    

        

    

    

    
