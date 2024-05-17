# 素数判定

import sys
args = sys.argv

a = args[1]

ans = "Yes"
for i in range(2,a//2):
    if a % i == 0:
        ans = "No"
        
print(ans,end="")