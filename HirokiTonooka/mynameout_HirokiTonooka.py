# x = 'HirokiTonooka'
# print('Hello ' + x + '!')

#sys・・・コマンドラインから渡された情報（引数）を取得することができる。
# import sys
#sys.argv・・・sysで入力された値を順番に受け付ける リストに入れてく
# args = sys.argv
#args[1]の理由は、sys.argvを使用する時点で、ファイル名がリスト0に格納されているため
# name = args[1]
# print(args[0])
# print('Hello',name,'!' ,end="")

#input・・・ターミナルで「お名前は？」と聞かれ、そこで入力した値をnameにいれて表示する。
# name = input("お名前は？")
# print(name + "さん、こんにちは！")

# user = input('時給はいくらですか？')
# jikyu = int(user)
# user = input("何時に働きましたか？")
# jikan = int(user)
# kyuryou = jikyu * jikan
#中かっこ{}にすると、文字列でも勝手に引数と認識してくれる。
# fmt = """
# 時給{0}円で、{1}時間働いたので...
# 給料は{2}円です。
# """
# desc = fmt.format(jikyu,jikan,kyuryou)
# print(desc)


# children = int(input("子供料金（１３歳未満）は何人？"))
# normal = int(input("通常料金（１３ー６４歳)は何人？"))
# elder = int(input("年配者料金（６５歳以上）は何人"))
# total_num = children + normal + elder
# children_price =children * 500
# normal_price = normal * 1000
# elder_price = elder * 700
# total_price =children_price + normal_price + elder_price
# if total_num >=10:
#     print("団体割引があります")
#     total_price = total_price * 0.8

# else:
#     print("割引はありません。")

# print("子供料金 :{0}人 * 500 = {1}円".format(children,children_price))
# print("通常料金 :{0}人 * 1000 = {1}円".format(normal,normal_price))
# print("年配者料金 :{0}人 * 700 = {1}円".format(elder,elder_price))
# print("合計 :{0}人 * {1}円".format(total_price,children_price))

