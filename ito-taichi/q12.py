# 世界の人口ランキングn位はどこ

import sys
args = sys.argv

a = int(args[1])

tp = ("China","India","U.S.A","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico")

print(tp[a-1],end="")