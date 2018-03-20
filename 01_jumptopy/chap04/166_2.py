#f=open("too.txt",'w')
#f.write("Life is too shore, you need python")
with open("too.txt",'w',encoding='UTF-8') as f:
    f.write("인생은 너무 짧네요. 그래서 당신은 파이썬이 필요해요")
##f.close()