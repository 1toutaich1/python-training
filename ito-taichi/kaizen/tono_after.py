import sys
args = sys.argv
# a = int(args[1])
# b = int(args[2])
# c = int(args[3])
 
#関数を定義
#引数numのcalcvalue変数を定義する
def calcvalue(num): #定義のみだと、実行までできない。最後に呼び出す作業が必要。
    #あまりを算出
    mod = num % 2
 
    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")
 
# もともと実行できる数が決まっていたが、for文を使用することによって、与えられた引数の数だけ実行できるようにした。
for i in range(1,len(args)):
    calcvalue(int(args[i]))