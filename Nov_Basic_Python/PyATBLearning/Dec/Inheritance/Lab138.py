# Hierarchical Inheritance

class Father:
    def BHK1(self):
        print("1BHK")

class Nishita(Father):
    def BHK2(self):
        print("2bhk")

class Amit(Father):
    def BHK3(self):
        print("3bhk")

class Lucky(Father):
    def no_house(self):
        print("NO house")

nishita=Nishita()
nishita.BHK1()
nishita.BHK2()

amit=Amit()
amit.BHK1()
amit.BHK3()
#amit.BHK2()
# amit.BHK2() # This belong to Pramod


l=Lucky()
# Only Father house
l.BHK1()
l.no_house()

