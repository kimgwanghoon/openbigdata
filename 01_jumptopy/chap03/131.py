#coding:cp949

namelist=[('��','����'),('��','���'),('��','����'),('��','ȿ��'),('��','����')]
#print(namelist)
#for(last_name,first_name) in namelist:
#   print(last_name+first_name)
name=str(input("�̸��� �Է��Ͻÿ� : "))
flag=1
for (last_name,first_name) in namelist:

    if name==last_name:    
        if flag==1: 
            print("<<�˻����>>") 
            flag=0
        print(last_name+first_name)
    else:
        pass
