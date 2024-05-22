#奇数・偶数を判定するプログラム
import sys
args = sys.argv
 
#「a」という値に引数を渡す
a = int(args[1])
 
#引数を２で割った余りがの時に「偶数」と表示する
#「%」は割った余りの関数
if a%2 ==0:
    print("偶数",end="")
 
#その他の時は奇数と表示する
else :
    print("奇数",end="")  