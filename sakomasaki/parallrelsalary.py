from func_salary import calcsalary
import sys
args = sys.argv

a=int(args[1])
b=int(args[2])

def printsal(a):
    x=calcsalary(a)
    print("給与:"+str(a)+"、支給額:"+str(x[0])+"、税額:"+str(x[1]))

printsal(a)
printsal(b)
