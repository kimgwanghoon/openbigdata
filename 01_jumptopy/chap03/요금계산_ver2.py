#coding:cp949

while True:
    age=int(input("���̸� �Է��ϼ���(0 ����) : "))
    money=0
    age_val=""
    if age<0:
        print("������ �߸��Է��Ͽ����ϴ�")
        continue
    elif age==0:
        break
    elif age>=66 :
        money +=0
        age_val="����"
    elif age>=19:
        money+=5000
        age_val="����"
    elif age>=14:
        money+=3000
        age_val="û�ҳ�"
    elif age>=4:
        money+=2000
        age_val="���"
    else :
        money +=0
        age_val="����"
    print("���ϴ� {0}����̸� ����� {1}�� �Դϴ�.".format(age_val, money))

