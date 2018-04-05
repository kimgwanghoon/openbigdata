def DN(in_su):
    num_list=[]
    for i in in_su:
        num_list.append(int(i))
    if sorted(num_list)==list(range(0,10)):
        print("true")
    else:
        print("false")

in_num = input("숫자를 입력 : ")
DN(in_num)