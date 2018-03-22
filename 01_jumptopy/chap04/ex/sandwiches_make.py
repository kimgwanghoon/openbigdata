def input_ingredient():
    ingredient_list = []
    while True:
        select_in=str(input("안녕하세요. 원하시는 재료를 입력하세요. : "))
        if select_in != "종료" :
            ingredient_list.append(select_in)
        elif select_in == '종료':
            return ingredient_list

def make_sandwiches(ingredient_list):
    print("샌드위치를 만들겠습니다.")
    for in_list in ingredient_list:
        print(in_list+" 추가합니다.")
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

while True:
    print("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다. \n 1.주문 \n 2.종료 \n 입력 : ",end='')
    select_num=int(input())

    if select_num==1:
        ingredient_list=input_ingredient()
        make_sandwiches(ingredient_list)
    elif select_num==2:
        print("안녕히 가세요")
        break