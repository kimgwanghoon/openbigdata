#coding:cp949

money_msg="�����մϴ�. Ƽ���� �����մϴ�."

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
    if money >0: 
        input_money = int(input("����� �Է��ϼ��� : "))
        if money==input_money:
            print(money_msg)
        elif money<input_money:
            print("{0} �Ž����� {1}�� ��ȯ�մϴ�".format(money_msg,(input_money-money)))
        else : 
            print("{0}�� ���ڶ��ϴ�. �Է��Ͻ� {1}�� ��ȯ�մϴ�".format((money-input_money),input_money))

    else:
        print(money_msg)
