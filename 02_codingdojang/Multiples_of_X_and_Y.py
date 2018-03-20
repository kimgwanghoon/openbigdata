#coding:cp949
while True:
#    i=1
    x=int(input("X의 값을 입력하세요(0 입력시 종료) : "))
    if x<=0:
        break
    y=int(input("Y의 값을 입력하세요 : "))
    z=int(input("Z의 값을 입력하세요 : "))
    lists=[]
#    while i<= z:
    for i in range(1,z+1):
        if i%(x*y)==0:
            lists.append(i)
#        i+=1
    print("1~{0}까지 {1}과 {2}의 공배수는 ".format(z,x,y),end='')
    print(lists)
   



