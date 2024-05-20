from decimal import Decimal,ROUND_HALF_UP

def calc_salary(val):    
    max = 1e6
    tax = 0
    if val > max:
        tax = (max * 0.1 + (val - max) * 0.2)
    else:
        tax = val * 0.1

    tax = int(Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))
    price = val - tax
    return price,tax