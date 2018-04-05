while True:
    input_su=int(input("양수를 입력하세요 (종료-1): "))
    if input_su!=-1:
        if input_su%10==0:
            print("입력한 숫자는 10의 배수입니다.")
        else:
            print("입력한 숫자는 10의 배수가 아닙니다")
    else:
        break