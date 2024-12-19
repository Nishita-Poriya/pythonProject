def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator02(func):
    def wrapper():
        print("Decorator2")
        func()
    return wrapper

@decorator1
@decorator02
def temp_decorators():
    print("Hello!")


temp_decorators()

