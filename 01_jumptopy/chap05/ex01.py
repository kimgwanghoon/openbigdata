class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type

    def describe_restautant(self):
        print("저희 레스토랑 명칭은 '%s'이고 %s 전문점 입니다."%(self.restaurant_name,self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요"%self.restaurant_name)

name, type=input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분)").split()
rest=Restaurant(name,type)
rest.describe_restautant()
rest.open_restaurant()
