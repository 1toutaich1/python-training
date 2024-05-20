import os 
import qrcode
import sys
args = sys.argv
img=qrcode.make(args[1])
path=os.path.join("../sakomasaki",args[2])
img.save(path)