# 複数の給与の支払い額を計算
import func_salary
import random

a = random.randint(100000,500000)
# b = 300000
# c = 400000


print(f"給与:{a} 支給額:{func_salary.calc_salary(a)[0]} 税額:{func_salary.calc_salary(a)[1]} ")
# print(f"支給額:{func_salary.calc_salary(b)[0]} 税額:{func_salary.calc_salary(b)[1]} ")
# print(f"支給額:{func_salary.calc_salary(c)[0]} 税額:{func_salary.calc_salary(c)[1]} ")