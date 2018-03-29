class Restaurant:
    todays_customer=0
    f = open("고객서빙현황로그.txt", 'w')
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        f = open("고객서빙현황로그.txt", 'r')
        self.number_served = int(f.read())

    def describe_restautant(self):
        print("저희 레스토랑 명칭은 '%s'이고 %s 전문점 입니다."%(self.restaurant_name,self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다."%self.restaurant_name)

    def reset_number_served(self,number):
        print("손님 %s명 들어오셨습니다. 자리를 안내해 드리겠습니다."%number)

    def increment_number_served(self,number):
        if int(number)!=0:
            self.todays_customer += int(number)
        else:
            self.todays_customer = 0
            print("손님 카운팅을 %d으로 초기화 하였습니다." % self.todays_customer)

    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다."%self.todays_customer)

    def __del__(self):
        print("%s 레스토랑 문닫습니다."%self.restaurant_name)
        total =str(self.number_served +self.todays_customer)
        self.f.write(total)
        self.f.close()

name, type=input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분)").split()
restaurant=Restaurant(name,type)
restaurant.describe_restautant()
open_sel = input("레스토랑을 오픈하시겠습니까? (y/n)")
if open_sel=='y':
    restaurant.open_restaurant()
    while True:
        number=input("어서오세요.몇명이십니까?(초기화:0입력, 종료:-1, 누적고객 확인:p) : ")
        if number=='0':
            restaurant.increment_number_served(number)
        elif number=='-1':
            break
        elif number=='p':
            restaurant.check_customer_number()
        else :
            restaurant.reset_number_served(number)
            restaurant.increment_number_served(number)