import sys

src=sys.argv[1]
dst=sys.argv[2]
f=open(src)
tab_con=f.read()
print(tab_con)
f.close()
space_con=tab_con.replace("\\t"," "*2)
f=open(dst,'w')
f.write(space_con)
f.close()