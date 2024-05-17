w = float(input("weight(kg):"))
h = float(input("height(cm)")) / 100 

bmi = w / (h * h)

print(f"BMI : {bmi}")
if bmi < 18.5:
    print("痩せ")
elif bmi >= 18.5 and bmi < 25:
    print("標準")
elif bmi >= 25 and bmi < 30:
    print("肥満（軽）")
else:
    print("肥満（重）")