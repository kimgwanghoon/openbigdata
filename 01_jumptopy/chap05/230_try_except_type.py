num1,num2= input("두개의 숫자를 입력하세요.").split()
is_cal=True

try:
    result = int(num1)/int(num2)
except:
    print("연산을 할수 없습니다")
    is_cal=False

if is_cal:
    print("%s / %s = %d"%(num1,num2,result))