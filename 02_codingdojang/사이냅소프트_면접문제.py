#coding:cp949

name = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
name=name.split(",")
kim_list=0
lee_list=0

for name_list in name:
    if name_list[0]=='김':
        kim_list+=1
    elif name_list[0]=='이':
        lee_list+=1

print("1. 김씨는 {0}명, 이씨는 {1}명 입니다.".format(kim_list,lee_list))

print("2.이재영 반복횟수 : %d"%name.count("이재영"))

name=set(name)
print("3. %s " %name)

name_sort=list(name)
name_sort.sort()
print("4. ",end='')
print(name_sort)



