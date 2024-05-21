from datetime import date
import sys
from database import session
from aquaattend import AttendNum

# 追加
args = sys.argv
dtstr = args[1]
dt_time = date(int(dtstr[:4]),int(dtstr[4:6]),int(dtstr[6:8])) 
normal_cnt = int(args[2])
child_cnt = int(args[3])

attendnum = AttendNum(
    entry_date = dt_time,
    seq = session.query(AttendNum).filter_by(entry_date=dt_time).count() + 1,
    # seq = session.query(AttendNum).group_by(AttendNum.seq).count() + 1,
    adult = normal_cnt,
    child = child_cnt
)
session.add(attendnum)
session.commit()

attend_list = session.query(AttendNum).all()
for a in attend_list:
    print(f"連番：{a.seq} 日付:{a.entry_date} 大人の人数{a.adult} 子供の人数:{a.child}")



# result = session.query(AttendNum).delete()
# session.commit()