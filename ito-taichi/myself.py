import introduce
import sys 

args = sys.argv

name = args[1]
age = int(args[2])


ins = introduce.Intro(name,age)
print(ins.name_out())
print(ins.age_out())


# test1
# name1 = "伊藤"
# age1 = 22 

# name2 = "太一"
# age2 = 23

# 普通
# print(f"私の名前は、{name1}です")
# print(f"私の年齢は、{age1}です")
# print(f"私の来年の年齢は、{age1+1}です")

# print(f"私の名前は、{name2}です")
# print(f"私の年齢は、{age2}です")
# print(f"私の来年の年齢は、{age2+1}です")


# オブジェ
# ins1 = introduce.Intro(name1,age1)
# print(ins1.name_out())
# print(ins1.age_out())
# print(ins1.age_nextyear_out())

# ins2 = introduce.Intro(name2,age2)
# print(ins2.name_out())
# print(ins2.age_out())
# print(ins2.age_nextyear_out())
