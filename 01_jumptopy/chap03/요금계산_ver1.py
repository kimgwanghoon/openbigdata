#coding:cp949

age=int(input("���̸� �Է��ϼ���"))
money=0

if age>=66 :
    money +=0
elif age>=19:
    money+=5000
elif age>=14:
    money+=3000
elif age>=4:
    money+=2000
else :
    money +=0
print("����� {0}�� �Դϴ�.".format(money))


