class Father:

    def home(self):
        return "this is from the father"

    def father_money(self):
        return 5

class Mother:

        def home(self):
            return "This is from the Mother"

        def mother_money(self):
            return 2

class Son(Father,Mother): #multiple inheritance

        def print_info(self):
            print("Son")

s=Son()
print(s.father_money())
print(s.mother_money())

print(s.home())
print(s.home())
