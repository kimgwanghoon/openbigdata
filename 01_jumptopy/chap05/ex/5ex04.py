def sum(a,b):
    return a+b

while True:
    try:
        su1=input("두수를 입력하세요.: ").split()
        su1[0]=int(su1[0])
        su1[1]=int(su1[1])
        hap=sum(su1[0],su1[1])
        print("{0} + {1} = {2}".format(su1[0],su1[1],hap))

    except ValueError as e:
         if str(su1.pop())=="종료":
             exit()
         else:
            if not isinstance(su1[0],int):
                print("첫번째 입력이 %s 입니다. 숫자를 입력하세요" %su1[0])
            else:
                 print("두번째 입력이 %s 입니다. 숫자를 입력하세요"%su1[1])
    finally:
        su1.clear()

# while True:
#     try:
#         su1,su2=input("두수를 입력하세요.: ").split()
#         su1=int(su1)
#         su2=int(su2)
#         sum=su1+su2
#         print("{0} + {1} = {2}".format(su1,su2,sum))
#
#     except ValueError as e:
#         if str(su1)=="종료" or str(su2)=="종료":
#             exit()
#         else:
#             if not isinstance(su1,int):
#                 print("첫번째 입력이 %s 입니다. 숫자를 입력하세요"%su1)
#             else:
#                 print("두번째 입력이 %s 입니다. 숫자를 입력하세요"%su2)
