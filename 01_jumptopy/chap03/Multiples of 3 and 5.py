#coding:cp949
hap=0
for num in range(1,1000):
    if num%3==0:
        hap+=num
    elif num%5==0:
        hap+=num
print("1000�̸��� �ڿ������� 3,5����� ������ {0}�̴�".format(hap))

