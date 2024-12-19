
class Father:
    key = "2bhk"

    def car(self):
        print("Father has a car-> Aulto")
        print(self.key)


class Son(Father):
    key2="3BHK"

    def suv(self):
        print("MG HECTOR,Black")
        print(self.key2)


father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.suv()
son_obj.car()