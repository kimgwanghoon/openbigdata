count=1
while True:
    c_name = input("안녕하세요. 이름을 입력하세요.")
    if count<=10:
        print("Hi %s!! You are 1st person come here!"%c_name)
        count=count+1
    else:
        print("Sorry %s. The event is closed because You are 11th person come here."%c_name)