import sys
args = sys.argv
a = int(args[1])
b = int(args[2])
c = int(args[3])
 
 
def calcvalue(num):
 
    mod = num % 2
 
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")
 
calcvalue(a)
calcvalue(b)
calcvalue(c)