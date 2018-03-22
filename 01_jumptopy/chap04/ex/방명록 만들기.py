def search_visitor(name):
    for name_sel in name_list:
        if name == name_sel:
            print(name + "님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요.")
            return
    birthday=input("생년월일을 입력하세요. (예:801212): ")
    f.write(name+" "+birthday+"\n")
    print("{0}님 환영합니다. 아래 내용을 입력하셨습니다. {1} {2}".format(name, name, birthday))

name=input("이름을 입력하세요 : ")
f = open("방명록.txt", 'r+', encoding="UTF-8")
name_list = f.read().split()

search_visitor(name)
f.close()