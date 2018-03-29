num1,num2= input("두개의 숫자를 입력하세요.").split()
try:
    result = int(num1)/int(num2)
    f=open('없는파일','r')

except FileNotFoundError as e:
    print("파일이 존재하지 않습니다")
    print("System Error Message: "+str(e))
    is_cal=False
except ZeroDivisionError as e :
    print("연산을 할수 없습니다")
    print("System Error Message: " + str(e))
    is_cal=False

else:
    is_cal=True
finally:
    f.close()

if is_cal:
    print("%s / %s = %d"%(num1,num2,result))
