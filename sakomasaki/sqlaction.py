from datetime import date
from database import session
from table import Holiday
#holiday=Holiday(
#    holi_date=date(2022,1,1),
#    holi_text="元日"
#)
holiday=Holiday(
    holi_date=date(2022,11,23),
    holi_text="勤労感謝の日"
)
session.add(holiday)

session.commit()