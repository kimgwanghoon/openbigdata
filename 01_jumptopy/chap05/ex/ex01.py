while True:
    input_msg = input("나이를 입력하세요(종료:종료)")
    if input_msg != "종료":
        input_msg=int(input_msg)
        if input_msg < 3:
            print("입장료 무료입니다.")
        elif input_msg >= 3  and input_msg<=12:
            print("입장권은 10달러입니다.")
        elif input_msg>=13:
            print("입장권은 15달러입니다.")
    else :
        break