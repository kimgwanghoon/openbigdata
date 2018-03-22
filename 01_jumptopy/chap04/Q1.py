def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2)+fib(n-1)

in_su=int(input("출력할 n번째 피보나치수열을 입력 : "))
i=0
while i<=in_su:
    result=fib(i)
    print(result,end=" ")
    if i<in_su:
        print(",",end="")
    i+=1