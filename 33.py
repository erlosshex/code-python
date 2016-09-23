import sys

def check(l):
    my_dict={}
    for i in l:
        if i not in my_dict:
            my_dict[i]=l.count(i)
    return my_dict

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    for i in all_lines:
        l=i.strip().split()
        my_dict=check(l)
        tmp_list=[]
        for k in my_dict:
            tmp_list.append(my_dict[k])
        tmp_list.sort()
        for j in tmp_list:
            print j,
        print

