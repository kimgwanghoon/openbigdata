#coding:cp949

name = "������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������"
name=name.split(",")
kim_list=0
lee_list=0

for name_list in name:
    if name_list[0]=='��':
        kim_list+=1
    elif name_list[0]=='��':
        lee_list+=1

print("1. �达�� {0}��, �̾��� {1}�� �Դϴ�.".format(kim_list,lee_list))

print("2.���翵 �ݺ�Ƚ�� : %d"%name.count("���翵"))

name=set(name)
print("3. %s " %name)

name_sort=list(name)
name_sort.sort()
print("4. ",end='')
print(name_sort)



