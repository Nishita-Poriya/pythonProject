

class Person:
    def home(self):
        print("2BHK")

class Son(Person):
    def town(self):
        print("10BHK")


    def home(self):
        print("3bhk")

object_ref=Son()
object_ref.home()
object_ref.town()
