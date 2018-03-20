#coding:cp949

money_msg="감사합니다. 티켓을 발행합니다."

while True:
    age=int(input("나이를 입력하세요(0 종료) : "))
    money=0
    age_val=""
    if age<0:
        print("나이을 잘못입력하였습니다")
        continue
    elif age==0:
        break
    elif age>=66 :
        money +=0
        age_val="노인"
    elif age>=19:
        money+=5000
        age_val="성인"
    elif age>=14:
        money+=3000
        age_val="청소년"
    elif age>=4:
        money+=2000
        age_val="어린이"
    else :
        money +=0
        age_val="유아"
    print("귀하는 {0}등급이며 요금은 {1}원 입니다.".format(age_val, money))
    if money >0:
        money_type=int(input("요금유형을 선택하세요(1:현금 2:공원 전용 신용 카드) : "))
        if money_type==1:
            input_money = int(input("요금을 입력하세요 : "))
            if money==input_money:
                print(money_msg)
            elif money<input_money:
                print("{0} 거스름돈 {1}를 반환합니다".format(money_msg,(input_money-money)))
            else : 
                print("{0}가 모자랍니다. 입력하신 {1}를 반환합니다".format((money-input_money),input_money))
        elif money_type==2:
            if age<60:
                print("{0}원 결제 되었습니다. 티켓을 발행합니다".format(int(money*0.9)))
            elif age>=60 and age<66:
                print("{0}원 결제 되었습니다. 티켓을 발행합니다".format(int((money*0.9)*0.95)))
        else :
            print("요금유형을 잘못 눌렀습니다. ")
    else:
        print(money_msg)
