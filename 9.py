import sys

def is_over(b1,b2):
    length1=abs(b1[0]-b1[1])
    length2=abs(b2[0]-b2[1])

    if length1>length2:
        if (b2[0]>=b1[0] and b2[0]<=b1[1]) or (b2[1]>=b1[0] and b2[1]<=b1[1]):
            return [min(b1[0],b2[0]),max(b1[1],b2[1])]
        else:
            return False
    else:
        if (b1[0]>=b2[0] and b1[0]<=b2[1]) or (b1[1]>=b2[0] and b1[1]<=b2[1]):
            return [min(b1[0],b2[0]),max(b1[1],b2[1])]
        else:
            return False
        


    
          
if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    all_lines=map(lambda x: x.split(), all_lines)
    all_lines=map(lambda x: map(int,x),all_lines)

    block_list=all_lines[1:]


    M=all_lines[0][0]
    N=all_lines[0][1]

    block_result=[1]*(M+1)

    for i in xrange(N):
        for j in xrange(block_list[i][0],block_list[i][1]+1):
            if block_result[j]==1:
                block_result[j]=0

    print sum(block_result)

    

        

    

    

    
