class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first+self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def sub(self):
        result = self.first-self.second
        return result
    def div(self):
        result = self.first/self.second
        return result

a=FourCal()
b=FourCal()

a.setdata(10,2)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
b.setdata(20,2)
print(b.sub())
print(b.div())
print(b.mul())
print(b.sum())

