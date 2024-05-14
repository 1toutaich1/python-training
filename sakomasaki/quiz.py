user = input("type jikyuu:")
jikyu = int(user)

user = input("how long:")
jikan = int(user)

kyuryou=jikyu*jikan

fmt= """時給{0}円で{1}時間働いたので給料は{2}円です."""
desc=fmt.format(jikyu,jikan,kyuryou)
print(desc)
