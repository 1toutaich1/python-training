
class Intro:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def name_out(self):
        nametxt = f"私の名前は、{self.name}です"
        return nametxt

    def age_out(self):
        agetxt = f"年齢は、{self.age}歳です"
        return agetxt
    def age_nextyear_out(self):
        agetxt = f"来年の年齢は、{self.age+1}歳です"
        return agetxt