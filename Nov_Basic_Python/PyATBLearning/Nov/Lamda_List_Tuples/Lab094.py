# Write a program to calcuclate even and odd

def even_odd(num):
    if num % 2==0:
        print("Even num:",num)
    else:
        print("odd num:",num)


even_odd(40)


print("---------------------------")

num =int(input("Enter a number:\n"))
op =lambda num: "Even" if num %2==0 else "Odd"

print(op(num))