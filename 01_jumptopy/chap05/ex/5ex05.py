def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    try:
        su1=input("두수를 입력하세요.: ").split()
        su1[0]=int(su1[0])
        su1[1]=int(su1[1])
        hap = sum(su1[0], su1[1])
        sub_e=sub(su1[0], su1[1])
        mul_e=mul(su1[0], su1[1])
        div_e=div(su1[0], su1[1])
        print("{0} + {1} = {2}".format(su1[0],su1[1],hap))
        print("{0} - {1} = {2}".format(su1[0], su1[1], sub_e))
        print("{0} * {1} = {2}".format(su1[0], su1[1], mul_e))
        print("{0} / {1} = {2}".format(su1[0], su1[1], div_e))
    except ValueError :
         if str(su1[0])=="종료":
             exit()
         else:
            if not isinstance(su1[0],int):
                print("첫번째 입력이 %s 입니다. 숫자를 입력하세요" %su1[0])
            else:
                 print("두번째 입력이 %s 입니다. 숫자를 입력하세요"%su1[1])

    except ZeroDivisionError :
        print("죄송합니다. 두 번쨰 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 않됩니다.")
    finally:
        su1.clear()