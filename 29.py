import sys

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    a_line=all_lines[0].strip()
    b_line=all_lines[1].strip()

    b_set=set(b_line)
    b_dict={}
    for i in b_set:
        b_dict[i]=b_line.count(i)

    a_set=set(a_line)
    a_dict={}
    for i in a_set:
        a_dict[i]=a_line.count(i)

    flag=True
    for i in b_dict:
        if i not in a_dict:
            flag=False
            break
        else:
            if b_dict[i]>a_dict[i]:
                flag=False
                break
            else:
                continue
    if flag==False:
        print 0
    else:
        print 1
