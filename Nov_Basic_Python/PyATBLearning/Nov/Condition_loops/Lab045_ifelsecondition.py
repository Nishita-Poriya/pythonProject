# Problem to find the max between two.

# Logic Building Formula

# 1 . user inputs -> two integers
# 2. o/ p ->  int 1 which ever is grater max number it will return.
# 31.4 or 45.34 - float

N1 = float(input("Enter the number1 \n"))
N2 = float(input("Enter the number2 \n"))

if N1 >= N2 :
    print("Maximum number is :",N1)
else:
    print("Maximum number is N2:",N2)

# Edge Cases - num1 == num2 ->  Handled.
# String -> ABC, ten -> try and except - We will learn this in future.
# -ve Value -> We will learn this in future.