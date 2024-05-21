from introduce import Intro 
import sys
args = sys.argv

human= Intro(args[1],args[2])
print(human.name_out())
print(human.age_out())

