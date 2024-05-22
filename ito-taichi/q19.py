import sys
from datetime import date
args = sys.argv

dtstr = args[1]
dt_time = date(int(dtstr[:4]),int(dtstr[4:6]),int(dtstr[6:8]))
dt = dt_time.strftime("%a") 

normal_cnt = int(args[2])
child_cnt = int(args[3])

if dt == "Sat" or dt == "Sun":
    total = 2400 * normal_cnt + 1500 * child_cnt
else:
    total = 2000 * normal_cnt + 1200 * child_cnt

print(total,end="")