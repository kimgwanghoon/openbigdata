#coding:cp949
print("<<구구단 출력프로그램 ver1>>")
for i in range(2,10):
    print("**%d단**"%i)
    for j in range(1,10):
        print("{0}*{1}={2}".format(i,j,i*j))
    print('')
