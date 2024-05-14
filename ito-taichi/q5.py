import sys
args = sys.argv

ma = int(args[1])
jp = int(args[2])
en = int(args[3])

if (ma + jp + en >= 220 or (ma >= 70 and jp >= 70 and en >= 70)) and (ma >= 50 and jp >= 50 and en >= 50):
    print("合格",end="")
else:
    print("不合格",end="")

    