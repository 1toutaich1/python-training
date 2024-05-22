from decimal import Decimal,ROUND_HALF_UP

# 引数val給与が与えられる
def calc_salary(val):
    # 1,000,000円を変数として定義
    max = 1e6
    tax = 0
    
    if val > max:
        # 引数が1,000,000円以上なら、超えた分に20%課税
        tax = (max * 0.1 + (val - max) * 0.2)
    else:
        # 1,000,000円以下なら10%だけ課税
        tax = val * 0.1

    # 税金taxを四捨五入
    tax = int(Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))
    #支給額は給与ー支給額
    price = val - tax
    return price,tax