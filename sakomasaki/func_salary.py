from decimal import Decimal,ROUND_HALF_UP
def calcsalary(sal):
    if sal>=1e6:
        tax=0.2*sal-1e5
    else:
        tax=0.1*sal
    tax= Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    return (sal-tax),tax


