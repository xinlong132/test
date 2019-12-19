#目录引用
#os操作
112233
#dev操作
import os
basedir=os.path.dirname(os.path.abspath(__file__))
print(basedir)
base2=os.path.join(basedir,"ceshi")
print(base2)