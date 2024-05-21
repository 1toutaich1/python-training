import introduce
class IntroFam(introduce.Intro):
    def __init__(self,name,age,cat_name):
        super().__init__(name,age)
        self.cat_name = cat_name
    
    def cat_out(self):
        return f"飼い猫の名前は、{self.cat_name}です"

class IntroFam(introduce.Intro):
    def __init__(self,name,age,cat_name,dog_name):
        super().__init__(name,age)
        self.cat_name = cat_name
        self.dog_name = dog_name
    
    def cat_out(self):
        return f"飼い猫の名前は、{self.cat_name}です"
        
    def dog_out(self):
        return f"飼い犬の名前は、{self.dog_name}です"