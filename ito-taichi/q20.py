# QRコードを出力
import sys
import qrcode

args = sys.argv
url = args[1]
file_name = args[2]

# img = qrcode.make(url)
# img.save(f"ito-taichi/files/{file_name}.png")

qr = qrcode.QRCode()
qr.add_data(url)
qr.make()
img = qr.make_image(fill_color="red",back_color="black")
img.save(f'ito-taichi/files/{file_name}.png')

# python3 ito-taichi/q20.py https://google.com google

