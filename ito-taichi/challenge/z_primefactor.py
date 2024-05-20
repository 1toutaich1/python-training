import sys
args = sys.argv

a = int(args[1])
ans = []

for i in range(2,a+1):
    while a % i == 0:
        ans.append(i)
        a //= i

print(ans,end="")