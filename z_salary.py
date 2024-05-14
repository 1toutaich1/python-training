import sys 
args = sys.argv

m = int(args[1])
j = int(args[2])
e = int(args[3])

if ((m >=70 and j>=70 and e>=70) or (m + j + e >=220)) and (m>=50 and j>=50 and e>=50):


    print ("合格",end="")

else:

    print("不合格",end="")







