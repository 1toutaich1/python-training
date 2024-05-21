from datetime import date
import datetime
import sys
from datetime import date
from database import session
from c3tables import *
from sqlalchemy.sql import func

mitems = {
    "お茶": ["110","TEA","3"],
    "コーヒー":["100","COFFEE","3"],
    "ソーダ":["160","SODA","3"],
    "コーンポタージュ":["130","CORNP","3"]
}
moneys =["5000","2000","1000","500","100","50","10"]
# insert Mst_merchandise
for namekey,data in mitems.items():
    inputd = Mst_merchandise(
        id = data[1],
        name = namekey,
        price = data[0]
    )
    session.add(inputd)
    session.commit()

# insert Tbl_stock
for namekey,data in mitems.items():
    inputd = Tbl_stock(
        id = data[1],
        stock = data[2]
    )
    session.add(inputd)
    session.commit()

# insert Tbl_money
for money in moneys():
    inputd = Tbl_money(
        price = money,
        stock = "20"
    )
    session.add(inputd)
    session.commit()

# insert Tbl_message
 # none