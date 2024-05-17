import sys
from decimal import Decimal,ROUND_HALF_UP

args = sys.argv
a = int(args[1])

max = 1e6

tax = 0
if a > max:
    tax = (max * 0.1 + (a - max) * 0.2)
else:
    tax = a * 0.1

tax = int(Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))
price = a - tax
print(f"支給額:{price}、税額:{tax}",end="")