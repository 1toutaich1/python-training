from datetime import date
import datetime
import sys
from database import session
from table import Holiday
args = sys.argv


sum=0

#来場日input を日付型に変換
numdate=args[1]
datt=date(int(numdate[:4]), int(numdate[4:6]), int(numdate[6:]))
dow=datt.strftime("%a")

#来場日が祝日tableに存在する/しないをか1,0で返す
isholiday = session.query(Holiday.holi_date).filter_by(holi_date=numdate).count()

#料金清算
sum=0
if dow =="Sat" or dow =="Sun" or isholiday==1:
    sum+=(2400*int(args[2])+1500*int(args[3]))
else:
    sum+=(2000*int(args[2])+1200*int(args[3]))

print("料金は："+str(sum))
