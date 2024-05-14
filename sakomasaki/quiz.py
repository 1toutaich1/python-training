children = int(input("child?"))
normal = int(input("normal?"))
elderly = int(input("elder?"))

totalnum = children + normal + elderly

sum = children*500 + normal*1000 + elderly*700
if totalnum>=10:
    print("you gonna discount")
    sum*=0.8

print("子供:{0},大人:{1},年配:{2},計{3}人,{4}円".format(children,normal,elderly,totalnum,sum))
