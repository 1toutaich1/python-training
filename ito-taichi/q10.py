import sys
args = sys.argv

a = int(args[1])

if 100 % a == 0:
    print("Just 100!",end="")
else:
    print("Over!",end="")

# cur = a
# while(cur < 100):
#     cur += a
    
# if cur == 100:
#     print("Just 100!",end="")
# else:
#     print("Over!",end="")