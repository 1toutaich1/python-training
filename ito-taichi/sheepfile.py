# 眠れない夜は２・・・
import os
import sys
args = sys.argv

a = int(args[1])

with open("ito-taichi/files/sheep.txt",mode="w",encoding="utf-8") as f:
    for i in range(a):
        out = ""
        out += f"ひつじが{i+1}匹"
        f.write(out)
