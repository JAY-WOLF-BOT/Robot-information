class Robot:
    
    def _init_(self,name,brand,atribute):
        self.name = name
        self.brand = brand
        self.atribute = atribute

    def intro(self):
        print("I am ",self.name," ,I am ",self.brand," and I am",self.atribute)

My_robot = Robot('Roz 4788','Adaptive','Multi-purpose')

My_robot.intro()
