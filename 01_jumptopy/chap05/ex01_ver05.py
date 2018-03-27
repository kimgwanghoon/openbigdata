class Restaurant:
    todays_customer=0
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
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

class Susi_rest(Restaurant):
    def menu_s(self):
        menu_sel=int(input("1.초밥 2.가츠동 3.라멘"))
        self.select(menu_sel)
    def select(self,menu_sel):
        if  menu_sel==1:
            print("초밥 선택")
        elif menu_sel==2:
            print("가츠동 선택")
        elif menu_sel==3:
            print("라멘")


class pizza_rest(Restaurant):
    def menu_s(self):
        menu_sel=int(input("1.불고기피자 2.페퍼로니피자 3.치즈킹피자"))
        self.select(menu_sel)
    def select(self,menu_sel):
        if menu_sel == 1:
            print("불고기피자 선택")
        elif menu_sel == 2:
            print("페퍼로니피자 선택")
        elif menu_sel == 3:
            print("치즈킹피자")

select_food = int(input("요리종류를 선택하세요.(1.일식 2.피자)"))
if select_food==1:
    type='일식'
    name=input("레스토랑 이름을 선택하세요.").split()
    Susi_rest=Susi_rest(name,type)
    Susi_rest.describe_restautant()
    open_sel = input("레스토랑을 오픈하시겠습니까? (y/n)")
    if open_sel=='y':
        Susi_rest.open_restaurant()
    while True:
        number=input("어서오세요.몇명이십니까?(초기화:0입력, 종료:-1, 누적고객 확인:p) : ")
        if number=='0':
            Susi_rest.increment_number_served(number)
        elif number=='-1':
            break
        elif number=='p':
            Susi_rest.check_customer_number()
        else :
            Susi_rest.reset_number_served(number)
            Susi_rest.increment_number_served(number)
            Susi_rest.menu_s()

elif select_food==2:
    type='피자'
    name=input("레스토랑 이름을 선택하세요.(공백으로 구분)").split()
    pizza_rest=pizza_rest(name,type)
    pizza_rest.describe_restautant()
    open_sel = input("레스토랑을 오픈하시겠습니까? (y/n)")
    if open_sel=='y':
        pizza_rest.open_restaurant()
    while True:
        number=input("어서오세요.몇명이십니까?(초기화:0입력, 종료:-1, 누적고객 확인:p) : ")
        if number=='0':
            pizza_rest.increment_number_served(number)
        elif number=='-1':
            break
        elif number=='p':
            pizza_rest.check_customer_number()
        else :
            pizza_rest.reset_number_served(number)
            pizza_rest.increment_number_served(number)
            pizza_rest.menu_s()