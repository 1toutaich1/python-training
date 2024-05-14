import sys
from decimal import Decimal,ROUND_HALF_UP
args = sys.argv
a = int(args[1])
b = int(args[2])
c = int(args[3])

if (a>=50 and b>=50 and c>=50) and ((a>=70 and b>=70 and c>=70) or (a+b+c)>220):
    print("合格です")
else:
    print("不合格です")
