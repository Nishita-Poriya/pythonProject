import math
def give_me_power(num):
    return math.pow(num,2)

op =give_me_power(10)
print(op)

op2 = lambda  : math.pow(int(input("Enter number : \n")),2)
print("Op:",op2())