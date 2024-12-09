class Home:
    def __init__(self):
        self._private_var="child"
        self.public_var="father"


    def mom(self):
        print(self._private_var)
        self._wife()

    def _wife(self):
        print("Private wife")

Object_ref= Home()
Object_ref.mom()
print(Object_ref.public_var)
Object_ref._wife()
print(Object_ref._private_var)
