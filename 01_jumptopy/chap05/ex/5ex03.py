input_Q=[]
name=[]
i=select=0
def read_content():
    f = open("poll.txt", "r", encoding='UTF-8')
    f_read=f.read()
    print(f_read)
    f.close()

try:
    read_content()
except FileNotFoundError as e:
    print(e)
    print("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.")
    select=int(input("1. 종료 2.새로운 파일 생성 3. 변경된 파일 경로 입력:"))
    if select==1:
        exit()
    elif select==2:
        f=open("poll.txt", "w", encoding='UTF-8')
    elif select==3:
        select_file=input("경로 입력 : ")
    else:
        print("잘못입력하였습니다")
        exit()

while True:
    input_Q.append(input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료) : "))
    if input_Q[i] != "종료":
        name.append(input("이름을 입력해주세요.: "))
        print("설문에 응답해 주셔서 감사합니다.")
        i = i + 1
    else:
        if select!=3:
            f = open("poll.txt", "a", encoding='UTF-8')
        else:
            f = open("%s" % select_file, "a", encoding='UTF-8')
        i1 = 0
        while i1 < i:
            f.write("[{0}] {1}\n".format(input_Q[i1], name[i1]))
            i1 += 1
        f.close()
        break