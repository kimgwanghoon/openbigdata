class Calculator :
    def __init__(self,list_num):
        self.list_num=list_num

    def sum(self):
        result=0
        for i in self.list_num:
            result+=i
        return result

    def avg(self):
        result=self.sum()
        return result/len(self.list_num)


cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
