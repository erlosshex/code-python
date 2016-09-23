import sys

def check(str_list):
    tmp_str=''
    for i in str_list:
        if i!='^':
            tmp_str=tmp_str+i
        else:
            tmp_str=tmp_str+'**'
    return tmp_str

if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    all_lines=map(lambda x:x.strip(),all_lines)

    for i in all_lines:
        print eval(check(i))

