
try:
    num1=int(input("Enter n number1\n"))
    num2=int(input("Enter num 2\n"))
    result=num1/num2

except ValueEroor as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Ou atput is ",result)