#coding:cp949

namelist=[('유','영재'),('문','희식'),('김','광훈'),('이','효진'),('문','재인')]
#print(namelist)
#for(last_name,first_name) in namelist:
#   print(last_name+first_name)
name=str(input("이름을 입력하시오 : "))
flag=1
for (last_name,first_name) in namelist:

    if name==last_name:    
        if flag==1: 
            print("<<검색결과>>") 
            flag=0
        print(last_name+first_name)
    else:
        pass
