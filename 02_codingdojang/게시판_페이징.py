#coding:cp949
total_page=0
gesi=int(input("게시물수 : "))
page=int(input("한페이지에 보여줄 게시물수 : "))

total_page=int(gesi/page)
if gesi%page !=0:
    total_page+=1
print("총 페이지수: {0}".format(total_page))
