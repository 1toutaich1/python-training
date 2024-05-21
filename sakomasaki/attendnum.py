from datetime import date
import datetime
import sys
from database import session
from makeattendnum import Attendnum
from sqlalchemy.sql import func
args = sys.argv

numdate=args[1]
datt=date(int(numdate[:4]), int(numdate[4:6]), int(numdate[6:]))

#
isholiday = session.query(Attendnum.entry_date).filter_by(entry_date=numdate).count()

##キャンセルに対応させる
rec: Attendnum = session.query(
        func.max(Attendnum.seq).label('price_max')
    ).filter_by(entry_date=numdate).one()
max=rec.price_max
##
inputdata=Attendnum(
    entry_date=numdate,
    seq=max+1,
    adult=int(args[2]),
    child=int(args[3])
)
session.add(inputdata)
session.commit()