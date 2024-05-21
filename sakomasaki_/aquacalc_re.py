from datetime import date
import datetime
import sys
args = sys.argv

#来場日input を日付型に変換 
numdate=args[1]
datt=date(int(numdate[:4]), int(numdate[4:6]), int(numdate[6:]))
dow=datt.strftime("%a")

#day of week に曜日を取得
dow=datt.strftime("%a")

#料金清算
sum = 0
if dow =="Sat" or dow =="Sun":
    sum+=(2400*int(args[2])+1500*int(args[3]))
else:
    sum+=(2000*int(args[2])+1200*int(args[3]))

print(sum,end="")
