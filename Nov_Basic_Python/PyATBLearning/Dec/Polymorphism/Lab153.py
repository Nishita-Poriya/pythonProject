# Static Methods
# A static method is a method that belongs to a
# class rather than an instance of the class.

class o:
    @staticmethod
    def sum(a,b):
        return a+b

    def sub(self,a,b):
        return a-b

obj_ref=o()
result=obj_ref.sub(3,4)
print("result:",result)
print("--------")

print(o.sum(3,4))