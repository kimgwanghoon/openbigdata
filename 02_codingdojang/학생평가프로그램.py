#coding:cp949

print("<<학생 시험 평가 프로그램>>")


stu=1
stu_ex=[]
while stu<=5:
    mark=input(str(stu)+"번 학생 점수 입력하세요 : ")
    stu_ex.append(int(mark))
    stu+=1
print("**평가결과**")

stu=1
for mark in stu_ex:
    if mark > 60:
        print("{0}번 학생 {1}점, 합격입니다.".format(stu,mark))
    else:
        continue
#        print("{0}번 학생 {1}점, 불합격입니다.".format(stu,mark))
    stu+=1
