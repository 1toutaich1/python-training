import sys
args = sys.argv

a = int(args[1])

cur = a
while(cur < 100):
    cur += a
    
if cur == 100:
    print("Just 100!")
else:
    print("Over!")