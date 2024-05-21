dict = {"お茶":110,"コーヒー":100,"ソーダ":160,"コーンポタージュ":130}
MIN_PRICE = 100
MAX_PRICE = 10000


# 投入金額を入力
def input_pay():
    txt = ""
    for i,j in dict.items():
        txt += f"{i} : {j}円\n"
    txt += "投入金額を入力してください"
    pay = int(input(txt))
    return pay


# 投入金額が範囲内か判定
def is_payment_over(pay):
    if pay >= MAX_PRICE:
        print("10,000円を超える金額は投入できません。再度入力してください")
        new_pay = int(input())
        is_payment_over(new_pay)
    elif pay < MIN_PRICE:
        print(f"{pay}円では購入できる商品がありません。再度入力してください")
        new_pay = int(input())
        is_payment_over(new_pay)
    elif pay % 10 != 0:
        print(f"1円玉、5円玉は使用できません。再度投入金額を入力してください")
        new_pay = int(input())
        is_payment_over(new_pay)
    return

def input_item():
    return input("何を購入しますか(商品名/cancel)")

def is_item_exsist(item):
    if not item in dict:
        new_item = input(f"正しい商品名を入力してください")
        is_item_exsist(new_item)
    return 

# 再度購入
def is_repurchase(money):
    if money < MIN_PRICE:
        return False
    return True

def back_money(money):
    ans = [0,0,0,0,0,0,0]
    coins = [5000,2000,1000,500,100,50,10]
    for i in range(len(coins)):
        while (money // coins[i] >= 1):
            money -= coins[i]
            ans[i] += 1
    print("おつり")
    for i in range(len(coins)):
        print(f"{coins[i]}円:{ans[i]}")

def buy(money):
    is_payment_over(money)

    i_item = input_item()
    if i_item == "cancel": return money

    # 商品の存在チェック
    is_item_exsist(i_item)

    money -= dict[i_item]

    print(f"残金:{money}円")
    
    # 再度購入できる場合
    if not is_repurchase(money):
        return money

    is_continue = input("続けて購入しますか(Y/N)")
    if is_continue == "Y":
        buy(money)
    else:
        return money

def main():
    i_money = input_pay()
    b_money = buy(i_money)
    back_money(b_money)

if __name__ == "__main__":
    main()