import sys

Ji='#'
At='@'
str_list=[Ji,At]

def modified(a_string):
    tmp_string=list(a_string)

    count_ji=0
    flag=False

    length=len(tmp_string)

    i=length-1

    while(i>=0):
        if tmp_string[i] in str_list:
            if tmp_string[i]==Ji:
                tmp_string[i]=''
                count_ji=count_ji+1
                flag=True
                i=i-1
            elif tmp_string[i]==At:
                tmp_string[i]=''
                flag=True
                i=i-1
        else:
            if flag==False:
                i=i-1
            else:
                if count_ji==0:
                    for ii in xrange(0,i+1):
                        tmp_string[ii]=''
                    i=-1
                    flag=False
                else:
                    for ii in xrange(i-count_ji+1,i+1):
                        tmp_string[ii]=''
                    i=i-count_ji
                    count_ji=0
                    flag=False

    #print tmp_string
    result=''
    for i in tmp_string:
        result=result+i
    return result

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    num=int(all_lines[0])
    string_lines=map(lambda x:x.strip(),all_lines[1:])

    for i in string_lines:
        print modified(i)
    

