import sys

if __name__=='__main__':
    a_line=sys.stdin.readline()
    a_line=a_line.split()
    a_line=map(int,a_line)

    result=abs(a_line[0]+a_line[1]-a_line[2])

    if result%2==0:
        print "Yes"
    else:
        print "No"
