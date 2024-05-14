import sys
args = sys.argv
name = args[1]
#intで囲む、前に着けることにより、argsの中身が整数になる。
# name = int(args[1])
name1 = args[2]
name2 = args[3]
#sys.argvによってリストに格納されたデータはすべて文字列なため、整数に直す必要委がある。
print(int(name) + int(name1) + int(name2))

# print('Hello',name,'!' ,end="")