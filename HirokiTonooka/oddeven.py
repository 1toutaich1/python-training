import sys
args = sys.argv
name = int(args[1])

if name%2==1:
    print('奇数',end="")

elif name%2 == 0:
    print('偶数',end="")