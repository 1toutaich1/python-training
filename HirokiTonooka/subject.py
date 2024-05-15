import sys
args = sys.argv
math = int(args[1])
japanese = int(args[2])
english = int(args[3])


# math = input('数学の得点は？')
# japanese = input('国語の得点は？')https://seminar-assist.jp/seminars/1285/program_evaluations/190#program_evaluation_question_2578
# english = int(input('英語の得点は？'))

if (math + japanese + english >=220 or (math>=70 and japanese>=70 and english>=70)) and (math>=50 and japanese>=50 and english>=50):
    print('合格')
else:
   print('不合格') 
