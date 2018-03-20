#coding=cp949
while True:
  i = int(input("홀수를 입력하세요(0 <- 종료):"))
  j=1
  if (i%2) == 1:
    while True:
      print(" "*int((i-j)/2) + "*"*j)
      if(i==j):break
      j+=2
    while True:
      j-=2
      print(" "*int((i-j)/2) + "*"*j)
      if(j<0): break
  elif i==0 : break
  else : 
    print("짝수를 입력했습니다")
    continue
