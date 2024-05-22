# 水族館の入園料を計算
import sys
from datetime import date
import re

def main():
    args = sys.argv

    dtstr = args[1]

    # 日付のフォーマットと合致するか検証
    date_pattern = r'^\d{8}$'
    if not re.match(date_pattern, dtstr):
        print("正しいフォーマットで入力してください")
        return

    # date型に変換
    dt_time = date(int(dtstr[:4]),int(dtstr[4:6]),int(dtstr[6:8]))

    # 曜日を取得
    dt = dt_time.strftime("%a") 

    # 第２,３引数を取得
    normal_cnt = int(args[2])
    child_cnt = int(args[3])


    # 大人の値段　0=平日の値段、1=土日の値段
    no_price = [2000,2400]
    # 子供の値段
    ch_price = [1200,1500]

    # 土日の判定 False=平日　True=土日
    is_holiday = True if dt == "Sat" or dt == "Sun" else False

    # 合計金額を計算
    # False=0,True=1として配列を取り出す
    total = no_price[is_holiday] * normal_cnt + ch_price[is_holiday] * child_cnt

    print(total,end="")

if __name__ == "__main__":
    main()
