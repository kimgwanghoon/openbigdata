ex = [-1,1,2,-3,6,-4,7,4,-2]
native_ex=[]
pos_ex=[]
print(ex)
for i in ex:
    if i<0:
        native_ex.append(i)
    else :
        pos_ex.append(i)
print(native_ex+pos_ex)


