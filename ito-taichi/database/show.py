from database import session
from tables import Holiday
from aquaattend import AttendNum

# holiday_list = session.query(Holiday).all()

# for day in holiday_list:
#     print(f"{day.holi_date} : {day.holi_text}")

attend_list = session.query(AttendNum).all()
for a in attend_list:
    print(f"連番：{a.seq} 日付:{a.entry_date} 大人の人数{a.adult} 子供の人数:{a.child}")