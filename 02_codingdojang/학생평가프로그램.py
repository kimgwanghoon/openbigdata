#coding:cp949

print("<<�л� ���� �� ���α׷�>>")


stu=1
stu_ex=[]
while stu<=5:
    mark=input(str(stu)+"�� �л� ���� �Է��ϼ��� : ")
    stu_ex.append(int(mark))
    stu+=1
print("**�򰡰��**")

stu=1
for mark in stu_ex:
    if mark > 60:
        print("{0}�� �л� {1}��, �հ��Դϴ�.".format(stu,mark))
    else:
        continue
#        print("{0}�� �л� {1}��, ���հ��Դϴ�.".format(stu,mark))
    stu+=1
