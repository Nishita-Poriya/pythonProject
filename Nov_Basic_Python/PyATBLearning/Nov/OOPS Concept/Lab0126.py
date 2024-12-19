class Person:
    def __init__(self,name):
        self.name=name

    def walk(self):
        return self.name

n1=Person("Nishita")
p1=Person("Poriya")

print(n1.name)
print(p1.name)

print("who is walking ",n1.walk())
print("who is walking",p1.walk())

