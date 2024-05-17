# 複数の整数の奇数・偶数を判定
import sys
args = sys.argv
n = int(args[1])
m = int(args[2])

def calcvalue(val):
    res = f"{n}は偶数" if val % 2 == 0 else f"{m}は奇数"
    print(res)

calcvalue(n)
calcvalue(m)