#coding:cp949

print("<<�л� ���� �� ���α׷�>>")


stu=1
stu_ex=[]
while stu<=5:
    stu_ex.append(int(input(str(stu)+"�� �л� ���� �Է��ϼ��� : ")))

    stu+=1

print("**�򰡰��**")
stu=1
for mark in stu_ex:
    if mark > 60:
        print("{0}�� �л� {1}��, �հ��Դϴ�.".format(stu,mark))
    else:
        print("{0}�� �л� {1}��, ���հ��Դϴ�.".format(stu,mark))
    stu+=1
