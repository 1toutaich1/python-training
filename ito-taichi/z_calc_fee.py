child = int(input("子供の人数:"))
normal = int(input("通常"))
elder = int(input("おじおば"))

sum = child + normal + elder
price = child * 500 + normal * 1000 + elder * 700 
if sum >= 10:
    print(price * 0.8)
else:
    print(price)