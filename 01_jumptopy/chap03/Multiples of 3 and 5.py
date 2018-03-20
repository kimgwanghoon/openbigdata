#coding:cp949
hap=0
for num in range(1,1000):
    if num%3==0:
        hap+=num
    elif num%5==0:
        hap+=num
print("1000미만의 자연수에서 3,5배수의 총합은 {0}이다".format(hap))

