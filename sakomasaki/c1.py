import sys
args = sys.argv
inputnum=int(args[1])

#素数格納用
primes=[]
primes.append(2)
num=3
for i in range (1,100):
    k=0
    for j in primes:
        if num%j==0:
            k=1
    if k==0:
        primes.append(num)
    num+=2

#答え出力用
ans=[]
i=0
while(inputnum>1):
    if inputnum%primes[i]==0:
        ans.append(primes[i])
        inputnum/=primes[i]
        continue
    else:
        i+=1

print(ans)

