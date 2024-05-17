from datetime import date
import sys
args = sys.argv
sum=0
dat=[0,0,0]
numdate=int(args[1])
dat[2]=numdate%100
numdate=int(numdate/100)
dat[1]=numdate%100
numdate=int(numdate/100)
dat[0]=numdate
dat=tuple(dat)
dow=datt.strftime("%a")
if dow =="Sat" or dow =="Sun":
    sum+=(2400*int(args[2])+1500*int(args[3]))
else:
    sum+=(2000*int(args[2])+1200*int(args[3]))

print(sum,end="")
