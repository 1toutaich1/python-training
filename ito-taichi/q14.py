# 英文のn番目の単語

import sys
args = sys.argv

txt = args[1]
idx = int(args[2])

li = txt.split()
print(li[idx-1],end="")

# "I am a human" 2

s_hyphen = '-one--two-'
print(s_hyphen.split('-'))
# ['', 'one', '', 'two', '']