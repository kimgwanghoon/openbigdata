#coding:cp949
total_page=0
gesi=int(input("�Խù��� : "))
page=int(input("���������� ������ �Խù��� : "))

total_page=int(gesi/page)
if gesi%page !=0:
    total_page+=1
print("�� ��������: {0}".format(total_page))
