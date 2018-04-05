while True:
    input_su1=input("세 개의 양수를 입력하세요 (종료 -1): ").split()
    if int(input_su1[0])!=-1 :
        input_su1[0] = int(input_su1[0])
        input_su1[1] = int(input_su1[1])
        input_su1[2] = int(input_su1[2])
        if input_su1[2]%input_su1[0]*input_su1[1]==0:
            print("{0}는 {1}와 {2}의 공배수입니다".format(input_su1[2],input_su1[0],input_su1[1]))
        else:
            print("{0}는 {1}와 {2}의 공배수가 아닙니다".format(input_su1[2], input_su1[0], input_su1[1]))
    else:
        break
    input_su1.clear()