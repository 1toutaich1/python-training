import sys
args = sys.argv
a = int(args[1])
anim=["giraffe", "tiger", "zebra", "elephant", "lion"]
anim.insert(a,args[2])
del anim[-1]
anim.sort()

print(anim,end="")