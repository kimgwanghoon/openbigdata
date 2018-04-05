input_Q=[]
name=[]
i=0
while True:
    input_Q.append(input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료) : "))
    if input_Q[i]!="종료":
        name.append(input("이름을 입력해주세요.: "))
        print("설문에 응답해 주셔서 감사합니다.")
        i=i+1
    else:
        f = open("poll.txt","a",encoding='UTF-8')
        i1=0
        while i1<i:
            f.write("[{0}] {1}\n".format(input_Q[i1],name[i1]))
            i1+=1
        f.close()
        break