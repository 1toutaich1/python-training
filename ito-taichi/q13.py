import sys
args = sys.argv

dict = {"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}

sta1 = args[1]
sta2 = args[2]

print(f"{abs(dict[sta1] - dict[sta2]):.2f}")