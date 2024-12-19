# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods.


class Car:
    def __init__(self):
        self.password = "Nishita" #public instance variable
        self._password_secure = "Nishita123" # private instance variable


    def change_password(self):
        self._password_secure="abc123"

Object_referance=Car()
print(Object_referance.password)
Object_referance.change_password()
print(Object_referance._password_secure) # 'Car' object has no attribute '__password_secure'