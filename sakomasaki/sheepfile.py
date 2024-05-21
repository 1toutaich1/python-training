import sys
import os
args = sys.argv

sheeps = int (args[1])
with open("../sakomasaki/files/sheep.txt",mode="w",encoding="utf-8") as a:
    for i in range(0,sheeps):
        a.write("ひつじが"+str(i+1)+"匹\n")


