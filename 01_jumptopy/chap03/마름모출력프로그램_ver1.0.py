#coding=cp949
while True:
  i = int(input("Ȧ���� �Է��ϼ���(0 <- ����):"))
  j=1
  if (i%2) == 1:
    while True:
      print(" "*int((i-j)/2) + "*"*j)
      j+=2
      if(i<j):break
  elif i==0 : break
  else : 
    print("¦���� �Է��߽��ϴ�")
    continue
