# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .


# Logic ?  If else - 1 condition,

# Syntax
# if condition 1:
#     print("do 1")
# elif condition 2:
#     print("do 2")
# elif condition 3:
#     print("do 3")
# else:
#     print(" do for else")

N1 = int(input("Enter the number N1: \n"))
N2 = int(input("Enter the number N2: \n"))
N3 = int(input("Enter the number N3: \n"))

if N1 > N2 and N1>N3 :
     print("N1 is max:",N1)
elif N2>N1 and N2>N3:
    print("N2 is max:",N2)
else:
    print("N3 is max:",N3)


