import sys
args = sys.argv

idx = int(args[1])
animal_name = (args[2])

li = ["giraffe","tiger","zebra","elephant","lion"]

li.insert(idx,animal_name)
li.pop(-1)

li.sort()

print(li,end="")