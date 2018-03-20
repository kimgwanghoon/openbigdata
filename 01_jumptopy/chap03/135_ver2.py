#coding:cp949
print("<<구구단 출력프로그램 ver2>>")
i=int(input("출력하고자 하는 단을 입력하시오 : "))
print("**%d단**"%i)
for j in range(1,10):
    print("{0}*{1}={2}".format(i,j,i*j))

