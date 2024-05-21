# 水族館の入園料を計算
import sys
from datetime import date
from database import session
from tables import Holiday

args = sys.argv
dtstr = args[1]
dt_time = date(int(dtstr[:4]),int(dtstr[4:6]),int(dtstr[6:8]))
dt = dt_time.strftime("%a") 
normal_cnt = int(args[2])
child_cnt = int(args[3])

no_price = [2000,2400]
ch_price = [1200,1500]

def is_holiday(date):
    return session.query(Holiday).filter_by(holi_date=date).count() >= 1

is_ok = True if dt == "Sat" or dt == "Sun" or is_holiday(dt_time) else False
 
ans = no_price[is_ok] * normal_cnt + ch_price[is_ok] * child_cnt

print(ans,end="")
