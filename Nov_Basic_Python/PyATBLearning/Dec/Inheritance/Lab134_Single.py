class Parent:
    gold ="2kg"

    def _init_(self):
        print("DC -Parent")

    def BHK2(self):
        print("2BHK")

class Child(Parent):

    def _init_(self):
        print("DC -Child")

    diamond="Diamond"

    def BHK3(self):
        print("3BHK")

child_object=Child()
print(child_object.gold)
child_object.BHK2()

father_obj=Parent()
father_obj.BHK2()
father_obj.BHK3()