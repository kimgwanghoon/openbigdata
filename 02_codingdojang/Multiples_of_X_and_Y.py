#coding:cp949
while True:
#    i=1
    x=int(input("X�� ���� �Է��ϼ���(0 �Է½� ����) : "))
    if x<=0:
        break
    y=int(input("Y�� ���� �Է��ϼ��� : "))
    z=int(input("Z�� ���� �Է��ϼ��� : "))
    lists=[]
#    while i<= z:
    for i in range(1,z+1):
        if i%(x*y)==0:
            lists.append(i)
#        i+=1
    print("1~{0}���� {1}�� {2}�� ������� ".format(z,x,y),end='')
    print(lists)
   



