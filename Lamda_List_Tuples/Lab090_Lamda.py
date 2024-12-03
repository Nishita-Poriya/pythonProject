#Lamda
from pluggy import Result


def Lamda(num):
    return num **3

Result = Lamda(5)
print("Result=",Result)


print("--------------")

result_l = lambda num : num ** 3
print("Using Lamda function result :",result_l(2))