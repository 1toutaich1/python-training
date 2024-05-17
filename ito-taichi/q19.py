# 水族館の入園料を計算
import sys
from datetime import date
args = sys.argv

dtstr = args[1]

# dateに変換
dt_time = date(int(dtstr[:4]),int(dtstr[4:6]),int(dtstr[6:8]))

# 曜日を取得
dt = dt_time.strftime("%a") 

normal_cnt = int(args[2])
child_cnt = int(args[3])

# 大人の値段　0=平日の値段、1=土日の値段
no_price = [2000,2400]
# 子供の値段　0=平日の値段、1=土日の値段
ch_price = [1200,1500]

# 土日の判定 0=平日　1=土日
# is_holiday = False
# if dt == "Sat" or dt == "Sun":
#     is_holiday = True

# 三項演算子
is_holiday = True if dt == "Sat" or dt == "Sun" else False
 
ans = no_price[is_holiday] * normal_cnt + ch_price[is_holiday] * child_cnt

print(ans,end="")