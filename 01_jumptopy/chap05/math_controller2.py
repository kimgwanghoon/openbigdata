# import mod3
import sys

print("현재 Pycharm에서 설정된 경로")
print(sys.path)
sys.path.append("C:\python")
import mod3
print("변경된 경로")
print(sys.path)

print(mod3.PI)
print(mod3.PI)
a=mod3.Math()
print(a.solv(2))

print(mod3.sum(mod3.PI,4.4))