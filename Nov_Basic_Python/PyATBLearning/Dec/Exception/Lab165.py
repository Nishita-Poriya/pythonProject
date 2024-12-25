print("----------start of the program")
try:
    a=int(input("Ent the num1"))#value Error :Invalid literal for int() with base 10: 'Pramod'
    b=int(input("Ent the num2"))
    c=a/b #zeroDivisionError :division by zero
    print("Result div is",c)
except Exception as e:
    print(e)

print("-----End of the Program")
