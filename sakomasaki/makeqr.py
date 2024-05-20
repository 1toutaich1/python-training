import os 
import qrcode

img=qrcode.make("https://www.google.co.jp/")

path=os.path.join("../sakomasaki","test01.png")

img.save(path)