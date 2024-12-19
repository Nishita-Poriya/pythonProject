class Father:
    def home(self):
        print("1BHK")

class Nishita(Father):
    def home(self):
        print("3BHK")

p=Nishita()
p.home()

f=Father()
f.home()