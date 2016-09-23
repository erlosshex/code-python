import sys

table_char=[]
for i in xrange(10):
    table_char.append(str(i))

table_char.append('+')
table_char.append('-')

for i in xrange(26):
    table_char.append(chr(97+i))
for i in xrange(26):
    table_char.append(chr(65+i))


def modify_str(bin_str):
    length=len(bin_str)
    diff=abs(8-length)
    for i in xrange(diff):
        bin_str='0'+bin_str
    return bin_str[2:]

def is_valid(str_list):
    length=len(str_list)
    if length%4==0:
        return True
    else:
        return False

def i_map(c,table):
    if c=='=':
        c='0'
    index = table.index(c)
    bin_index=modify_str(bin(index)[2:])
    return bin_index

def mmap(c_string_bin):
    return chr(int(c_string_bin,2))


def decode(str_list):
    if is_valid(str_list)==False:
        return 'Invalid'
    else:
        equal_count=str_list.count('=')
        result_bin_string=''
        for i in str_list:
            tmp_str=i_map(i,table_char)
            result_bin_string=result_bin_string+tmp_str
        i=0
        origin_string=''
        while i<len(result_bin_string):
            origin_string=origin_string+mmap(result_bin_string[i:i+8])
            i=i+8
        while equal_count>0:
            origin_string=origin_string[:-1]
            equal_count=equal_count-1
        return origin_string
        

if __name__=='__main__':
    all_lines=sys.stdin.readlines()

    num=int(all_lines[0])
    str_lists=map(lambda x:x.strip(),all_lines[1:])

    for item in str_lists:
        print decode(item)

    
