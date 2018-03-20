#coding:cp949

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

