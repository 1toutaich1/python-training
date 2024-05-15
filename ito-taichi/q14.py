import sys
args = sys.argv

txt = args[1]
idx = int(args[2])

li = txt.split()
print(li[idx-1])

# "I am a human" 2