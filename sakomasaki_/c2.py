items={"お茶":110,"コーヒー":100,"ソーダ":160,"コーンポタージュ":130}
maxp = max(items.values())

#買えるもの表示
def pur_able(a):
    for item in items:
        if a >= items[item]:
            print(item+"："+str(items[item])+"円")

pur_able(maxp)

insm =input("投入金額を入力してください")
F = 0
while(F==0):    
    if insm%10!=0:
        print("１円玉、５円玉は使用できません。再度投入金額を入力してください")
    elif insm<=min(items.values()):
        print(str(insm)+"円では購入できる商品がありません。再度投入金額を入力してください")
    elif insm>10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
    else :
        F=1

F=0
while F ==0:
    str1 = input("何を購入しますか（商品名/cancel）")
    if str1 in items:
        insm-=items[str1]
        #最安値以上?
        if insm>=min(items.values()):
            print("残金："+str(insm)+"円")
            str2 =input("続けて購入しますか（Y/N）")
            if str2 == "Y":
                pur_able(insm)
            elif str2 == "N":
                F=1
        else:
            F=1
         
    elif str1 == "cancel":
        F=1
    else:
        print(str1+"は商品一覧にありません")

print("おつり")

if insm>=5000:
    print("5000円札：1枚")
    insm-=5000

if insm>=4000:
    print("2000円札：2枚")
    insm-=4000
elif insm>=2000:
    print("2000円札：1枚")
    insm-=2000

if insm>=1000:
    print("1000円札：1枚")
    insm-=1000

if insm>=500:
    print("500円玉：1枚")
    insm-=500

if insm>=100:
    a=int(insm/100)
    print("100円玉："+str(a)+"枚")
    insm-=(a*100)

if insm>=50:
    print("50円玉：1枚")
    insm-=50

if insm>=10:
    a=int(insm/10)
    print("10円玉："+str(a)+"枚")

insm=0


