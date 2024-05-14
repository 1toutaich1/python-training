import sys
args = sys.argv
name = args[1]
print("I don't like " + '"' + name + '"',end="")
#シングルクォーテーションの前にバックスラッシュを入れることで、本来打てない文字を打つことができる
# print("I don\'t like \"" + name +"\"",end="" )