# 複数の整数の奇数・偶数を判定

# import sys
# args = sys.argv
# n = int(args[1])
# m = int(args[2])

# def calcvalue(val):
#     res = f"{n}は偶数" if val % 2 == 0 else f"{m}は奇数"
#     print(res)

# calcvalue(n)
# calcvalue(m)

import sys
args = sys.argv

a = int(args[1])
b = int(args[2])
c = int(args[3])

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

calcvalue(a)
calcvalue(b)
calcvalue(c)
