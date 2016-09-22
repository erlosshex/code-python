import sys

leap=[0,31,29,31,30,31,30,31,31,30,31,30,31]
ordinary=[0,31,28,31,30,31,30,31,31,30,31,30,31]

leap_sum=366
ordinary_sum=365

today_sum=sum(ordinary[:10])+18

def is_leap(my_year):
    if my_year%100==0:
        if my_year%400==0:
            return True
        else:
            return False
    else:
        if my_year%4==0:
            return True
        else:
            return False

if __name__=='__main__':
    line=sys.stdin.readline()
    line=line.split('-')
    line=map(int,line)

    y=line[0]
    m=line[1]
    d=line[2]

    result=0

    if is_leap(y):
        if m==1:
            result=result+d
        elif m==2:
            if d<29:
                result=result+leap[1]+d
            elif d==29:
                result=result+sum(leap[:m+1])
        else:
            result=result+sum(leap[:m])+d
    else:
        result=result+sum(ordinary[:m])+d

    for i in xrange(2015,y):
        if is_leap(i):
            result=result+leap_sum
        else:
            result=result+ordinary_sum

    result=result-today_sum
    print result

    

    

    

        

    

    

    
