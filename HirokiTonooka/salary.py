# import sys
# args = sys.argv

a = int(input('あなたの給料を入力してください'))

if a >1000000:
    b = a - 1000000
    tax_amount = b * 0.2
    c = a - tax_amount
    d = round(c,0)
    print(c)

elif a<1000000:
    tax_amount = a * 0.1
    c = a - tax_amount
    d = round(c,0)
    print(d)
    