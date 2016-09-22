def fun(test_num,num,iter_num):
    tmp_num=test_num-1
    if tmp_num%num==0:
        if iter_num==num:
            return True
        else:
            return fun(tmp_num-tmp_num/num,num,iter_num+1)
    else:
        return False

if __name__=='__main__':
    number=input()

    i=number+1
    while True:
        if fun(i,number,1):
            print i
            break
        else:
            i=i+number
            

    

    

        

    

    

    
