from myfamily import IntroFam
import sys
args = sys.argv

human= IntroFam(args[1],args[2],args[3])
print(human.name_out())
print(human.age_out())
print(human.cat_out())

