class Service:
    secret="영구는 배꼽이 두개다"
    # def setname(self,name):
        # self.name = name
    def __init__(self,name):
        self.name = name

    def sum(self, a, b):
        result = a+b
        print("%s 님%s + %s = %s 입니다."%(self.name,a,b,result))

# pey=Service()
# pey.setname("홍길동")
pey =Service("홍길동")
pey.sum(1,1)