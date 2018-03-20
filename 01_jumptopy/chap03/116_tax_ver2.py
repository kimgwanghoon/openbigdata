# coding: cp949

print("\n-----택시 안내 가이드 프로그램 ver1-----")

#money=2000
print("가지고 계신 금액을 입력하세요 : ",end='')
money =int(input())
print("\n현재 가지고 계신 금액은 "+str(money)+"원 입니다")

if money>=3000:
    print("택시를 타고 갈 수 있습니다")
else:
    print("돈이 부족하니 걸어가야 합니다.")

print("프로그램을 종료합니다")
