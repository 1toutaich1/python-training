from datetime import date
from database import session
from tables import Holiday

# show
holiday_list = session.query(Holiday).all()
for day in holiday_list:
    print(f"{day.holi_date} : {day.holi_text}")
