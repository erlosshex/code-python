import sys

class solution(object):
    def __init__(self):
        self.number=1
        self.up=1
        self.down=1
        self.result=[1]
        self.count=0
        self.tmp_count=self.count
        self.date=0

        self.flag_count=True
        self.flag_date=True

    def solve(self,date_num,date_start=0):
        iter_date=date_start+1

        while(iter_date<=date_num):
            if iter_date==1:
                self.count=self.count+1
                self.result.append(self.number)
                self.date=self.date+1
                iter_date=iter_date+1
                
                continue
            if self.flag_date==True:
                if self.flag_count==True:
                    self.tmp_count=self.count
                    self.flag_count=False
                self.number=self.number+self.up
                self.result.append(self.number)
                self.date=self.date+1
                iter_date=iter_date+1
                self.tmp_count=self.tmp_count-1
                if self.tmp_count==0:
                    self.flag_date=False
                    
            else:
                self.number=self.number-1
                self.result.append(self.number)
                self.date=self.date+1
                iter_date=iter_date+1
                self.count=self.count+1
                self.flag_date=True
                self.flag_count=True

    def find_out(self,date_num):
        if date_num<=self.date:
            sys.stdout.write(str(self.result[date_num])+'\n')
        else:
            self.solve(date_num,self.date)
            sys.stdout.write(str(self.result[date_num])+'\n')

    def output(self):
        sys.stdout.write('\n')
        for i in self.result:
            sys.stdout.write(str(i)+' ')
        sys.stdout.write('\n')



if __name__=='__main__':
    all_lines=sys.stdin.readlines()
    all_lines=map(int,all_lines)

    max_num=max(all_lines)

    a=solution()
    a.solve(max_num)

    for i in all_lines:
        a.find_out(i)

    a.output()


        
