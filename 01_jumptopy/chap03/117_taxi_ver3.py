# coding: cp949

print("\n-----택시 안내 가이드 프로그램 ver1-----")

#money=2000
#print("가지고 계신 금액을 입력하세요 : ",end='')
money =int(input("가지고 계신 금액을 입력하세요: "))
card = int(input("신용카드를 소지하고 계십니까?(1:예,2:아니오):"))
print("입력 조건 분석")
print("\n현재 가지고 계신 금액은 "+str(money)+"원 입니다")

if card==1:
    print("신용카드를 소지하고 계십니다.")
else:
    print("현재 신용카드가 없습니다.")

print("\n분석결과")
if money>=3000 or card==1:
    print("택시를 타고 갈 수 있습니다")
else:
    print("돈이 부족하니 걸어가야 합니다.")

print("\n프로그램을 종료합니다")
